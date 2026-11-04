"""Simple in-memory storage adapter for pivot snapshots / demos."""

from __future__ import annotations

from typing import Any, Dict, Optional
from uuid import uuid4

from skilldispatch.adapters.base import AdapterResult


class InMemoryStorageAdapter:
    name = "storage"

    def __init__(self) -> None:
        self._rows: Dict[str, Dict[str, Any]] = {}

    def healthcheck(self) -> AdapterResult:
        return AdapterResult(ok=True, data={"rows": len(self._rows)}, source=self.name)

    def save(self, payload: Dict[str, Any]) -> AdapterResult:
        key = str(uuid4())
        self._rows[key] = dict(payload)
        return AdapterResult(ok=True, data={"id": key}, source=self.name)

    def get(self, key: str) -> AdapterResult:
        row = self._rows.get(key)
        if row is None:
            return AdapterResult(ok=False, error="not_found", source=self.name)
        return AdapterResult(ok=True, data=row, source=self.name)

    def latest(self) -> Optional[Dict[str, Any]]:
        if not self._rows:
            return None
        key = next(reversed(self._rows))
        return self._rows[key]
