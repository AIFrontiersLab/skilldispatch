"""Small text hygiene helpers used across parsers."""

from __future__ import annotations

import re

_WS = re.compile(r"\s+")
_EDGE_PUNCT = re.compile(r"^[\s\"'`(\[{<]+|[\s\"'`)\]}>.,:;!?]+$")


def collapse_whitespace(value: str) -> str:
    return _WS.sub(" ", (value or "")).strip()


def strip_punctuation_edges(value: str) -> str:
    text = value or ""
    prev = None
    while prev != text:
        prev = text
        text = _EDGE_PUNCT.sub("", text)
    return text.strip()
