"""Pipeline stage: match normalized skills to roles."""

from __future__ import annotations

from typing import List

from skilldispatch.domain.matcher import RoleMatcher
from skilldispatch.models.schemas import RoleMatch, SkillNormalized


class MatchStage:
    def __init__(self, matcher: RoleMatcher | None = None) -> None:
        self.matcher = matcher or RoleMatcher()

    def run(self, skills: List[SkillNormalized], years: int) -> List[RoleMatch]:
        return self.matcher.match_many(skills, years)
