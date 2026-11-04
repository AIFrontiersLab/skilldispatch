"""Named pipeline stages for Skilldispatch."""

from skilldispatch.pipelines.pivot_pipeline import PivotPipeline
from skilldispatch.pipelines.normalize_stage import NormalizeStage
from skilldispatch.pipelines.match_stage import MatchStage
from skilldispatch.pipelines.plan_stage import PlanStage

__all__ = ["PivotPipeline", "NormalizeStage", "MatchStage", "PlanStage"]
