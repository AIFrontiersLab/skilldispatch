"""Pipeline diagnostics for operators and debugging."""

from __future__ import annotations

from typing import Dict, List

from skilldispatch.config.settings import Settings
from skilldispatch.models.schemas import RoleMatch, SkillNormalized


def build_diagnostics(
    settings: Settings,
    normalized: List[SkillNormalized],
    matches: List[RoleMatch],
) -> Dict[str, str]:
    mapped = sum(1 for s in normalized if s.aliases_matched or s.canonical != s.raw)
    avg_score = (
        round(sum(m.composite_score for m in matches) / len(matches), 3)
        if matches
        else 0.0
    )
    return {
        "pipeline_mode": f"llm={settings.llm_mode};labor={settings.labor_market_mode}",
        "skills_in": str(len(normalized)),
        "alias_hits": str(mapped),
        "roles_out": str(len(matches)),
        "avg_composite": str(avg_score),
        "top_role": matches[0].title if matches else "",
        "top_confidence": matches[0].confidence.value if matches else "",
    }
