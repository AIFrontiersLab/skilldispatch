"""Aggregate health across adapters and settings."""

from __future__ import annotations

from typing import Any, Dict

from skilldispatch.adapters.labor_adapter import LaborMarketAdapter
from skilldispatch.adapters.llm_adapter import LLMAdapter
from skilldispatch.adapters.storage_adapter import InMemoryStorageAdapter
from skilldispatch.config.settings import Settings, get_settings


class HealthService:
    def __init__(
        self,
        settings: Settings | None = None,
        llm: LLMAdapter | None = None,
        labor: LaborMarketAdapter | None = None,
        storage: InMemoryStorageAdapter | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self.llm = llm or LLMAdapter()
        self.labor = labor or LaborMarketAdapter()
        self.storage = storage or InMemoryStorageAdapter()

    def status(self) -> Dict[str, Any]:
        adapters = {
            "llm": self.llm.healthcheck().ok,
            "labor_market": self.labor.healthcheck().ok,
            "storage": self.storage.healthcheck().ok,
        }
        return {
            "status": "ok" if all(adapters.values()) else "degraded",
            "app": self.settings.app_name,
            "api_version": self.settings.api_version,
            "llm_mode": self.settings.llm_mode,
            "labor_market_mode": self.settings.labor_market_mode,
            "adapters": adapters,
        }
