"""High-level orchestrator used by FastAPI routes and CLI demos."""

from __future__ import annotations

from skilldispatch.config.settings import Settings, get_settings
from skilldispatch.models.schemas import RoadmapResponse, SkillInput
from skilldispatch.pipelines.pivot_pipeline import PivotPipeline
from skilldispatch.services.telemetry import TelemetrySink
from skilldispatch.services.validation import PivotValidator


class SkillDispatchOrchestrator:
    def __init__(
        self,
        settings: Settings | None = None,
        pipeline: PivotPipeline | None = None,
        validator: PivotValidator | None = None,
        telemetry: TelemetrySink | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self.pipeline = pipeline or PivotPipeline(self.settings)
        self.validator = validator or PivotValidator(self.settings)
        self.telemetry = telemetry or TelemetrySink(self.settings)

    def pivot(self, payload: SkillInput) -> RoadmapResponse:
        self.validator.ensure_usable(payload)
        self.telemetry.emit(
            "pivot.requested",
            {
                "experience_years": payload.experience_years,
                "skills_chars": len(payload.skills or ""),
            },
        )
        result = self.pipeline.run(payload)
        self.telemetry.emit(
            "pivot.completed",
            {
                "roles": len(result.target_roles),
                "steps": len(result.roadmap),
                "weeks": result.estimated_time_weeks,
            },
        )
        return result
