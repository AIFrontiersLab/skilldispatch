"""Skilldispatch application entrypoint.

Keeps a thin compatibility layer so existing imports (`from main import app`,
`parse_skills`, `SkillInput`, `demo`) continue to work while the real logic
lives in the `skilldispatch` package.
"""

from __future__ import annotations

from skilldispatch.api.app import create_app
from skilldispatch.domain.normalizer import SkillNormalizer
from skilldispatch.models.schemas import (  # noqa: F401 — public re-exports
    RoadmapResponse,
    RoadmapStep,
    SkillInput,
)
from skilldispatch.services.orchestrator import SkillDispatchOrchestrator
from skilldispatch.services.llm_stub import LocalLLMTranslator

app = create_app()
_normalizer = SkillNormalizer()
_orchestrator = SkillDispatchOrchestrator()
_llm = LocalLLMTranslator()


def parse_skills(text: str):
    """Backward-compatible helper used by tests and demos."""
    return _normalizer.parse_raw(text)


def analyze_gaps(skills, years: int):
    """Backward-compatible wrapper around the orchestrated pipeline."""
    payload = SkillInput(skills=", ".join(skills), experience_years=years)
    result = _orchestrator.pivot(payload)
    return {
        "original_skills": result.original_skills,
        "target_roles": result.target_roles,
        "roadmap": result.roadmap,
        "estimated_time_weeks": result.estimated_time_weeks,
        "normalized_skills": result.normalized_skills,
        "role_matches": result.role_matches,
        "diagnostics": result.diagnostics,
    }


def demo() -> None:
    """CLI Demo for testing without server."""
    test_input = SkillInput(skills="data entry, customer support", experience_years=3)
    res = _orchestrator.pivot(test_input)
    narrative = _llm.translate_skills(res.original_skills, res.target_roles)
    print(f"Original: {res.original_skills}")
    print(f"Targets: {res.target_roles}")
    print(f"Narrative: {narrative.narrative}")
    for step in res.roadmap:
        print(f"  [{step.phase}] {step.action} ({step.priority})")
    print(f"Time: {res.estimated_time_weeks} weeks")
    print(f"Diagnostics: {res.diagnostics}")


if __name__ == "__main__":
    demo()
