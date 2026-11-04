"""Pipeline stage: compose roadmap and week estimate."""

from __future__ import annotations

from typing import List, Tuple

from skilldispatch.domain.roadmap import RoadmapComposer
from skilldispatch.models.schemas import RoleMatch, RoadmapStep


class PlanStage:
    def __init__(self, composer: RoadmapComposer | None = None) -> None:
        self.composer = composer or RoadmapComposer()

    def run(self, matches: List[RoleMatch], years: int) -> Tuple[List[RoadmapStep], int]:
        steps = self.composer.compose(matches, years)
        weeks = self.composer.estimate_weeks(years, steps)
        return steps, weeks
