"""Lightweight telemetry sink (no-op in MVP, structured for later wiring)."""

from __future__ import annotations

import logging
from typing import Any, Dict

from skilldispatch.config.settings import Settings, get_settings

log = logging.getLogger("skilldispatch.telemetry")


class TelemetrySink:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()
        self._events: list[Dict[str, Any]] = []

    def emit(self, event: str, payload: Dict[str, Any] | None = None) -> None:
        record = {
            "namespace": self.settings.telemetry_namespace,
            "event": event,
            "payload": payload or {},
        }
        self._events.append(record)
        log.debug("telemetry %s", record)

    def recent(self) -> list[Dict[str, Any]]:
        return list(self._events[-50:])
