"""In-process domain event bus used by orchestrator/telemetry seams."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List


@dataclass(frozen=True)
class DomainEvent:
    name: str
    payload: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


Listener = Callable[[DomainEvent], None]


class EventBus:
    def __init__(self) -> None:
        self._listeners: Dict[str, List[Listener]] = {}
        self._history: List[DomainEvent] = []

    def subscribe(self, name: str, listener: Listener) -> None:
        self._listeners.setdefault(name, []).append(listener)

    def publish(self, event: DomainEvent) -> None:
        self._history.append(event)
        for listener in self._listeners.get(event.name, []):
            listener(event)
        for listener in self._listeners.get("*", []):
            listener(event)

    def history(self) -> List[DomainEvent]:
        return list(self._history)
