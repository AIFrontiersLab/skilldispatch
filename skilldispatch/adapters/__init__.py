"""Outbound adapters for LLM, labor-market, and storage integrations."""

from skilldispatch.adapters.base import Adapter, AdapterResult
from skilldispatch.adapters.llm_adapter import LLMAdapter
from skilldispatch.adapters.labor_adapter import LaborMarketAdapter
from skilldispatch.adapters.storage_adapter import InMemoryStorageAdapter

__all__ = [
    "Adapter",
    "AdapterResult",
    "LLMAdapter",
    "LaborMarketAdapter",
    "InMemoryStorageAdapter",
]
