"""Map normalized legacy skills onto ranked AI-adjacent roles."""

from __future__ import annotations

from typing import Dict, List

from skilldispatch.config.settings import Settings, get_settings
from skilldispatch.data.legacy_skill_map import LEGACY_TO_AI_MAP
from skilldispatch.data.market_signals import MARKET_SIGNALS_BY_ROLE
from skilldispatch.data.role_catalog import ROLE_CATALOG, ROLE_DEMAND
from skilldispatch.domain.scoring import ScoreEngine
from skilldispatch.models.schemas import MarketSignal, RoleMatch, SkillNormalized


class RoleMatcher:
    def __init__(
        self,
        settings: Settings | None = None,
        score_engine: ScoreEngine | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self.scores = score_engine or ScoreEngine(self.settings)

    def _fallback_title(self, skill: str) -> str:
        titled = skill.replace("-", " ").title()
        return f"AI-adjacent {titled}"

    def match_one(self, skill: SkillNormalized, years: int) -> RoleMatch:
        mapped = skill.canonical in LEGACY_TO_AI_MAP
        title = LEGACY_TO_AI_MAP.get(skill.canonical) or self._fallback_title(skill.canonical)
        adjacency = self.scores.adjacency_from_direct_map(mapped, skill.obsolescence_risk)
        demand = float(ROLE_DEMAND.get(title, 0.5))
        signal = MARKET_SIGNALS_BY_ROLE.get(title, MarketSignal.STABLE)
        if self.settings.enable_market_demand_bias:
            demand = min(0.99, max(0.05, demand + self.scores.market_boost(signal)))
        composite = self.scores.composite(adjacency, demand, years)
        confidence = (
            self.scores.confidence_band(composite)
            if self.settings.enable_confidence_bands
            else self.scores.confidence_band(0.5)
        )
        family = str(ROLE_CATALOG.get(title, {}).get("family", skill.category))
        rationale = (
            f"Mapped '{skill.canonical}' via static ontology into {family} family "
            f"with adjacency={adjacency:.2f} and demand={demand:.2f}."
            if mapped
            else (
                f"No exact ontology hit for '{skill.canonical}'; synthesized "
                f"an AI-adjacent placeholder role for exploration."
            )
        )
        return RoleMatch(
            title=title,
            adjacency_score=round(adjacency, 3),
            demand_score=round(demand, 3),
            composite_score=composite,
            confidence=confidence,
            market_signal=signal,
            rationale=rationale,
            source_skills=[skill.canonical],
        )

    def match_many(
        self,
        skills: List[SkillNormalized],
        years: int,
    ) -> List[RoleMatch]:
        by_title: Dict[str, RoleMatch] = {}
        for skill in skills:
            match = self.match_one(skill, years)
            existing = by_title.get(match.title)
            if existing is None or match.composite_score > existing.composite_score:
                if existing is not None:
                    match.source_skills = sorted(
                        set(existing.source_skills + match.source_skills)
                    )
                by_title[match.title] = match
            elif existing is not None:
                merged = sorted(set(existing.source_skills + match.source_skills))
                existing.source_skills = merged
        ranked = sorted(
            by_title.values(),
            key=lambda m: (m.composite_score, m.demand_score),
            reverse=True,
        )
        return ranked[: self.settings.max_target_roles]
