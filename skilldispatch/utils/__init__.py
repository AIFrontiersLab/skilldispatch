"""Shared helpers."""

from skilldispatch.utils.text import collapse_whitespace, strip_punctuation_edges
from skilldispatch.utils.diagnostics import build_diagnostics
from skilldispatch.utils.hashing import pivot_cache_key, stable_hash
from skilldispatch.utils.serialization import dumps_pretty, loads_obj

__all__ = [
    "collapse_whitespace",
    "strip_punctuation_edges",
    "build_diagnostics",
    "pivot_cache_key",
    "stable_hash",
    "dumps_pretty",
    "loads_obj",
]
