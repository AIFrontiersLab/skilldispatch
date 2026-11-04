"""Labor-market adapter wrapping the offline client."""

from __future__ import annotations

from skilldispatch.adapters.base import AdapterResult
from skilldispatch.services.labor_market_stub import LaborMarketClient


class LaborMarketAdapter:
    name = "labor_market"

    def __init__(self, client: LaborMarketClient | None = None) -> None:
        self.client = client or LaborMarketClient()

    def healthcheck(self) -> AdapterResult:
        top = self.client.top_demand(1)
        return AdapterResult(
            ok=True,
            data={"sample_role": top[0].role_title if top else ""},
            source=self.name,
        )

    def observe(self, role_title: str) -> AdapterResult:
        obs = self.client.get_observation(role_title)
        return AdapterResult(
            ok=True,
            data={
                "role_title": obs.role_title,
                "demand_score": obs.demand_score,
                "signal": obs.signal.value,
                "geography": obs.geography,
                "source": obs.source,
            },
            source=self.name,
        )
