"""Typed contracts exchanged across the Skilldispatch pipeline."""

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, field_validator


class ConfidenceBand(str, Enum):
    EXPLORATORY = "exploratory"
    PROMISING = "promising"
    STRONG = "strong"
    IMMEDIATE = "immediate"


class MarketSignal(str, Enum):
    DECLINING = "declining"
    STABLE = "stable"
    GROWING = "growing"
    SURGING = "surging"


class SkillInput(BaseModel):
    """Primary POST /pivot body — kept for backward compatibility."""

    skills: str = Field(..., description="Comma-separated legacy skills")
    experience_years: int = Field(..., ge=0, le=50)

    @field_validator("skills")
    @classmethod
    def skills_must_not_be_blank_whitespace_only(cls, value: str) -> str:
        if value is None:
            raise ValueError("skills cannot be null")
        return value


class PivotRequest(SkillInput):
    """Extended pivot request with optional localization hints."""

    locale: str = Field(default="en-US")
    prefer_remote: bool = Field(default=True)
    industry_bias: Optional[str] = Field(default=None)


class SkillNormalized(BaseModel):
    raw: str
    canonical: str
    aliases_matched: List[str] = Field(default_factory=list)
    category: str = "general"
    obsolescence_risk: float = Field(default=0.5, ge=0.0, le=1.0)


class RoleMatch(BaseModel):
    title: str
    adjacency_score: float = Field(ge=0.0, le=1.0)
    demand_score: float = Field(ge=0.0, le=1.0)
    composite_score: float = Field(ge=0.0, le=1.0)
    confidence: ConfidenceBand = ConfidenceBand.EXPLORATORY
    market_signal: MarketSignal = MarketSignal.STABLE
    rationale: str = ""
    source_skills: List[str] = Field(default_factory=list)


class RoadmapStep(BaseModel):
    phase: str
    action: str
    priority: str
    estimated_hours: int = 8
    skill_focus: Optional[str] = None
    success_signal: Optional[str] = None


class RoadmapResponse(BaseModel):
    original_skills: List[str]
    target_roles: List[str]
    roadmap: List[RoadmapStep]
    estimated_time_weeks: int
    normalized_skills: List[SkillNormalized] = Field(default_factory=list)
    role_matches: List[RoleMatch] = Field(default_factory=list)
    pipeline_version: str = "static-v3"
    diagnostics: Dict[str, str] = Field(default_factory=dict)
