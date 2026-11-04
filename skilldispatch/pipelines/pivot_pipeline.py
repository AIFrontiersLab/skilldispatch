"""End-to-end pivot pipeline: normalize → match → roadmap → response."""

from __future__ import annotations

from skilldispatch.config.settings import Settings, get_settings
from skilldispatch.domain.matcher import RoleMatcher
from skilldispatch.domain.normalizer import SkillNormalizer
from skilldispatch.domain.roadmap import RoadmapComposer
from skilldispatch.models.schemas import RoadmapResponse, SkillInput
from skilldispatch.utils.diagnostics import build_diagnostics


class PivotPipeline:
    """Deterministic multi-stage translation from legacy skills to roadmaps."""

    def __init__(
        self,
        settings: Settings | None = None,
        normalizer: SkillNormalizer | None = None,
        matcher: RoleMatcher | None = None,
        composer: RoadmapComposer | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self.normalizer = normalizer or SkillNormalizer(self.settings)
        self.matcher = matcher or RoleMatcher(self.settings)
        self.composer = composer or RoadmapComposer(self.settings)

    def run(self, payload: SkillInput) -> RoadmapResponse:
        normalized = self.normalizer.normalize_text(payload.skills)
        matches = self.matcher.match_many(normalized, payload.experience_years)
        roadmap = self.composer.compose(matches, payload.experience_years)
        weeks = self.composer.estimate_weeks(payload.experience_years, roadmap)
        diagnostics = build_diagnostics(self.settings, normalized, matches)
        return RoadmapResponse(
            original_skills=[s.canonical for s in normalized],
            target_roles=[m.title for m in matches],
            roadmap=roadmap,
            estimated_time_weeks=weeks,
            normalized_skills=normalized,
            role_matches=matches,
            pipeline_version="static-v3",
            diagnostics=diagnostics,
        )
