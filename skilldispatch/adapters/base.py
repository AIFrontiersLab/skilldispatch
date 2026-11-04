"""Shared adapter protocol."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Protocol


@dataclass(frozen=True)
class AdapterResult:
    ok: bool
    data: Dict[str, Any] = field(default_factory=dict)
    error: str = ""
    source: str = "stub"


class Adapter(Protocol):
    name: str

    def healthcheck(self) -> AdapterResult:
        ...
