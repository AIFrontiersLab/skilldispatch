"""Route handlers for pivot and operator introspection endpoints."""

from __future__ import annotations

from fastapi import APIRouter

from skilldispatch.data.role_catalog import ROLE_CATALOG, ROLE_DEMAND
from skilldispatch.models.schemas import RoadmapResponse, SkillInput
from skilldispatch.services.health import HealthService
from skilldispatch.services.labor_market_stub import LaborMarketClient
from skilldispatch.services.orchestrator import SkillDispatchOrchestrator

router = APIRouter()
_orchestrator = SkillDispatchOrchestrator()
_labor = LaborMarketClient()
_health = HealthService()


@router.get("/health")
def health() -> dict:
    return _health.status()


@router.post("/pivot", response_model=RoadmapResponse)
def pivot(input_data: SkillInput) -> RoadmapResponse:
    return _orchestrator.pivot(input_data)


@router.get("/roles")
def list_roles(limit: int = 25) -> dict:
    limit = max(1, min(limit, 100))
    ranked = sorted(ROLE_DEMAND.items(), key=lambda item: item[1], reverse=True)[:limit]
    return {
        "count": len(ranked),
        "roles": [
            {
                "title": title,
                "demand": demand,
                "family": ROLE_CATALOG.get(title, {}).get("family", "general"),
                "tools": ROLE_CATALOG.get(title, {}).get("tools", []),
            }
            for title, demand in ranked
        ],
    }


@router.get("/roles/{role_title}/market")
def role_market(role_title: str) -> dict:
    obs = _labor.get_observation(role_title)
    return {
        "role_title": obs.role_title,
        "demand_score": obs.demand_score,
        "signal": obs.signal.value,
        "geography": obs.geography,
        "source": obs.source,
        "explanation": _labor.explain(role_title),
    }


@router.get("/ontology/stats")
def ontology_stats() -> dict:
    from skilldispatch.data.legacy_skill_map import LEGACY_TO_AI_MAP, SKILL_ALIASES

    return {
        "legacy_skills": len(LEGACY_TO_AI_MAP),
        "alias_groups": len(SKILL_ALIASES),
        "catalog_roles": len(ROLE_CATALOG),
    }
