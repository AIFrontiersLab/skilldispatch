"""Skill tokenization, alias expansion, and canonicalization."""

from __future__ import annotations

import re
from typing import Dict, Iterable, List, Set, Tuple

from skilldispatch.config.settings import Settings, get_settings
from skilldispatch.data.legacy_skill_map import LEGACY_TO_AI_MAP, SKILL_ALIASES
from skilldispatch.data.market_signals import OBSOLESCENCE_HINTS
from skilldispatch.models.schemas import SkillNormalized
from skilldispatch.utils.text import collapse_whitespace, strip_punctuation_edges


ALIAS_LOOKUP: Dict[str, str] = {}
for canonical, aliases in SKILL_ALIASES.items():
    ALIAS_LOOKUP[canonical] = canonical
    for alias in aliases:
        ALIAS_LOOKUP[alias.lower()] = canonical


class SkillNormalizer:
    """Turn messy free-text skill lists into structured canonical skills."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self._token_split = re.compile(r"[,;/|]+")

    def parse_raw(self, text: str) -> List[str]:
        parts = self._token_split.split(text or "")
        cleaned: List[str] = []
        seen: Set[str] = set()
        for part in parts:
            value = collapse_whitespace(strip_punctuation_edges(part)).lower()
            if not value or value in seen:
                continue
            seen.add(value)
            cleaned.append(value)
        return cleaned

    def resolve_alias(self, skill: str) -> Tuple[str, List[str]]:
        if not self.settings.enable_alias_expansion:
            return skill, []
        if skill in ALIAS_LOOKUP:
            canonical = ALIAS_LOOKUP[skill]
            matched = [skill] if skill != canonical else []
            return canonical, matched
        # Soft contains match for longer aliases.
        for alias, canonical in ALIAS_LOOKUP.items():
            if len(alias) >= 4 and alias in skill:
                return canonical, [alias]
        return skill, []

    def categorize(self, skill: str) -> str:
        role = LEGACY_TO_AI_MAP.get(skill)
        if not role:
            return "general"
        from skilldispatch.data.role_catalog import ROLE_CATALOG

        meta = ROLE_CATALOG.get(role, {})
        return str(meta.get("family", "general"))

    def obsolescence(self, skill: str) -> float:
        return float(OBSOLESCENCE_HINTS.get(skill, 0.5))

    def normalize_many(self, skills: Iterable[str]) -> List[SkillNormalized]:
        out: List[SkillNormalized] = []
        seen_canonical: Set[str] = set()
        for raw in skills:
            canonical, matched = self.resolve_alias(raw)
            if canonical in seen_canonical:
                # Preserve first raw form; fold later aliases into that record.
                for existing in out:
                    if existing.canonical == canonical and matched:
                        merged = sorted(set(existing.aliases_matched + matched + [raw]))
                        existing.aliases_matched = merged
                        break
                continue
            seen_canonical.add(canonical)
            out.append(
                SkillNormalized(
                    raw=raw,
                    canonical=canonical,
                    aliases_matched=matched,
                    category=self.categorize(canonical),
                    obsolescence_risk=self.obsolescence(canonical),
                )
            )
        return out

    def normalize_text(self, text: str) -> List[SkillNormalized]:
        return self.normalize_many(self.parse_raw(text))
