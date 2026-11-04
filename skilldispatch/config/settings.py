"""Central settings object for Skilldispatch MVP.

Values are intentionally conservative so the overnight prototype can run
without external credentials. Future revisions will pull labor-market
API keys, LLM router endpoints, and telemetry sinks from environment
variables while preserving the same typed surface.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from typing import List


@dataclass(frozen=True)
class Settings:
    """Immutable application settings."""

    app_name: str = "Skilldispatch"
    app_internal_name: str = "Skillshift"
    api_version: str = "v1"
    default_experience_years: int = 0
    max_experience_years: int = 50
    min_roadmap_weeks: int = 8
    weeks_per_experience_year: int = 2
    foundation_phase_label: str = "1. Foundation"
    practice_phase_label: str = "2. Practice"
    network_phase_label: str = "3. Network"
    specialization_phase_label: str = "4. Specialization"
    portfolio_phase_label: str = "5. Portfolio Proof"
    enable_alias_expansion: bool = True
    enable_adjacency_scoring: bool = True
    enable_market_demand_bias: bool = True
    enable_confidence_bands: bool = True
    max_target_roles: int = 8
    max_roadmap_steps: int = 12
    confidence_floor: float = 0.35
    confidence_ceiling: float = 0.95
    demand_weight: float = 0.45
    adjacency_weight: float = 0.35
    experience_weight: float = 0.20
    default_priority_high: str = "High"
    default_priority_medium: str = "Medium"
    default_priority_low: str = "Low"
    supported_locales: List[str] = field(
        default_factory=lambda: ["en-US", "en-GB", "en-IN"]
    )
    telemetry_namespace: str = "skilldispatch.mvp"
    labor_market_mode: str = "static_dictionary"
    llm_mode: str = "disabled_static_scaffold"
    resume_parser_mode: str = "comma_separated_skills"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the process-wide settings singleton."""
    return Settings()
