"""Stub labor-market client.

Production Skilldispatch is expected to call a live occupational-demand API.
This stub preserves the interface while returning static demand scores so the
overnight MVP remains fully offline and deterministic.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional

from skilldispatch.data.role_catalog import ROLE_DEMAND
from skilldispatch.data.market_signals import MARKET_SIGNALS_BY_ROLE
from skilldispatch.models.schemas import MarketSignal


@dataclass(frozen=True)
class LaborMarketObservation:
    role_title: str
    demand_score: float
    signal: MarketSignal
    geography: str = "global"
    source: str = "static_dictionary"


class LaborMarketClient:
    """Offline stand-in for a paid labor-market data provider."""

    def __init__(self, geography: str = "global") -> None:
        self.geography = geography
        self._cache: Dict[str, LaborMarketObservation] = {}

    def get_observation(self, role_title: str) -> LaborMarketObservation:
        if role_title in self._cache:
            return self._cache[role_title]
        obs = LaborMarketObservation(
            role_title=role_title,
            demand_score=float(ROLE_DEMAND.get(role_title, 0.5)),
            signal=MARKET_SIGNALS_BY_ROLE.get(role_title, MarketSignal.STABLE),
            geography=self.geography,
        )
        self._cache[role_title] = obs
        return obs

    def batch(self, role_titles: List[str]) -> List[LaborMarketObservation]:
        return [self.get_observation(title) for title in role_titles]

    def top_demand(self, limit: int = 10) -> List[LaborMarketObservation]:
        ranked = sorted(
            ROLE_DEMAND.items(),
            key=lambda item: item[1],
            reverse=True,
        )
        return [self.get_observation(title) for title, _ in ranked[:limit]]

    def explain(self, role_title: str) -> str:
        obs = self.get_observation(role_title)
        return (
            f"{obs.role_title} currently scores {obs.demand_score:.2f} demand "
            f"({obs.signal.value}) in geography={obs.geography} via {obs.source}."
        )


def maybe_live_client(api_key: Optional[str] = None) -> LaborMarketClient:
    """Factory that will later branch to a live HTTP client when credentials exist."""
    del api_key  # reserved for future wiring
    return LaborMarketClient()
