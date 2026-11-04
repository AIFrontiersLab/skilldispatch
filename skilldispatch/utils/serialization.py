"""JSON helpers for CLI and storage adapters."""

from __future__ import annotations

import json
from typing import Any


def dumps_pretty(payload: Any) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, default=str)


def loads_obj(text: str) -> Any:
    return json.loads(text)
