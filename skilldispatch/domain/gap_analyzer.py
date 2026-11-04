"""Estimate skill gaps between legacy experience and target roles."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from skilldispatch.data.role_catalog import ROLE_CATALOG
from skilldispatch.models.schemas import RoleMatch, SkillNormalized


@dataclass(frozen=True)
class GapInsight:
    role_title: str
    missing_themes: List[str]
    transfer_strength: float
    notes: str


class GapAnalyzer:
    def analyze(self, skills: List[SkillNormalized], match: RoleMatch) -> GapInsight:
        meta = ROLE_CATALOG.get(match.title, {})
        keywords = [str(k) for k in meta.get("keywords", [])]
        present = " ".join(s.canonical for s in skills)
        missing = [k for k in keywords if k.lower() not in present]
        transfer = round(max(0.2, match.adjacency_score - 0.05 * len(missing)), 3)
        notes = (
            f"{len(missing)} thematic gaps vs role keywords; "
            f"transfer_strength={transfer:.2f}."
        )
        return GapInsight(
            role_title=match.title,
            missing_themes=missing,
            transfer_strength=transfer,
            notes=notes,
        )
