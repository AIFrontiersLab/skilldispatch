"""Stable ranking utilities for role matches."""

from __future__ import annotations

from typing import Iterable, List

from skilldispatch.models.schemas import RoleMatch


def rank_matches(matches: Iterable[RoleMatch], limit: int) -> List[RoleMatch]:
    ranked = sorted(
        matches,
        key=lambda m: (m.composite_score, m.demand_score, m.adjacency_score, m.title),
        reverse=True,
    )
    return ranked[: max(0, limit)]


def titles_only(matches: Iterable[RoleMatch]) -> List[str]:
    return [m.title for m in matches]
