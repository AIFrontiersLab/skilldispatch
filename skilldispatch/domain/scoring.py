"""Composite scoring for role adjacency, demand, and experience fit."""

from __future__ import annotations

from skilldispatch.config.settings import Settings, get_settings
from skilldispatch.models.schemas import ConfidenceBand, MarketSignal


class ScoreEngine:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()

    def adjacency_from_direct_map(self, mapped: bool, obsolescence: float) -> float:
        if mapped:
            return min(0.95, 0.72 + obsolescence * 0.2)
        return max(0.25, 0.40 - obsolescence * 0.05)

    def experience_modifier(self, years: int) -> float:
        # Mid-career pivots often transfer judgment faster than juniors.
        if years <= 1:
            return 0.55
        if years <= 3:
            return 0.68
        if years <= 7:
            return 0.82
        if years <= 15:
            return 0.88
        return 0.80

    def composite(
        self,
        adjacency: float,
        demand: float,
        years: int,
    ) -> float:
        s = self.settings
        exp = self.experience_modifier(years)
        score = (
            s.adjacency_weight * adjacency
            + s.demand_weight * demand
            + s.experience_weight * exp
        )
        return round(min(s.confidence_ceiling, max(s.confidence_floor, score)), 3)

    def confidence_band(self, score: float) -> ConfidenceBand:
        if score >= 0.85:
            return ConfidenceBand.IMMEDIATE
        if score >= 0.72:
            return ConfidenceBand.STRONG
        if score >= 0.55:
            return ConfidenceBand.PROMISING
        return ConfidenceBand.EXPLORATORY

    def market_boost(self, signal: MarketSignal) -> float:
        return {
            MarketSignal.DECLINING: -0.08,
            MarketSignal.STABLE: 0.0,
            MarketSignal.GROWING: 0.05,
            MarketSignal.SURGING: 0.10,
        }[signal]
