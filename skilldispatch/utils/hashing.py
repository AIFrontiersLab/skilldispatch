"""Stable hashing helpers for cache keys and idempotency."""

from __future__ import annotations

import hashlib


def stable_hash(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8")).hexdigest()


def pivot_cache_key(skills: str, years: int) -> str:
    return stable_hash(f"{skills.strip().lower()}::{years}")
