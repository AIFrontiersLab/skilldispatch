"""Helpers around confidence-band presentation."""

from __future__ import annotations

from skilldispatch.models.schemas import ConfidenceBand, RoleMatch


def label_for(match: RoleMatch) -> str:
    return f"{match.title} [{match.confidence.value}]"


def is_actionable(match: RoleMatch) -> bool:
    return match.confidence in {
        ConfidenceBand.PROMISING,
        ConfidenceBand.STRONG,
        ConfidenceBand.IMMEDIATE,
    }


def partition_actionable(matches: list[RoleMatch]) -> tuple[list[RoleMatch], list[RoleMatch]]:
    yes = [m for m in matches if is_actionable(m)]
    no = [m for m in matches if not is_actionable(m)]
    return yes, no
