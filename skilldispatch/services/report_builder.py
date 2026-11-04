"""Build human-readable pivot reports from pipeline responses."""

from __future__ import annotations

from skilldispatch.core.constants import DEFAULT_REPORT_TITLE
from skilldispatch.models.schemas import RoadmapResponse
from skilldispatch.services.llm_stub import LocalLLMTranslator


class ReportBuilder:
    def __init__(self, translator: LocalLLMTranslator | None = None) -> None:
        self.translator = translator or LocalLLMTranslator()

    def build_markdown(self, result: RoadmapResponse) -> str:
        narrative = self.translator.translate_skills(
            result.original_skills, result.target_roles
        ).narrative
        lines = [
            f"# {DEFAULT_REPORT_TITLE}",
            "",
            "## Narrative",
            narrative,
            "",
            "## Target Roles",
        ]
        for role in result.target_roles:
            lines.append(f"- {role}")
        lines.extend(["", "## Roadmap"])
        for step in result.roadmap:
            lines.append(f"- **{step.phase}** ({step.priority}): {step.action}")
        lines.extend(
            [
                "",
                f"**Estimated time:** {result.estimated_time_weeks} weeks",
                f"**Pipeline:** {result.pipeline_version}",
            ]
        )
        return "\n".join(lines)
