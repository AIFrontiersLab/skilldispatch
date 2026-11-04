"""Repository for phased learning path content."""

from __future__ import annotations

from typing import List

from skilldispatch.data.learning_paths import (
    FOUNDATION_ACTIONS,
    NETWORK_ACTIONS,
    PORTFOLIO_ACTIONS,
    PRACTICE_ACTIONS,
    SPECIALIZATION_ACTIONS,
)


class LearningRepository:
    def foundation(self, family: str) -> str:
        return FOUNDATION_ACTIONS.get(family, FOUNDATION_ACTIONS["general"])

    def practice(self, family: str) -> str:
        return PRACTICE_ACTIONS.get(family, PRACTICE_ACTIONS["general"])

    def network_options(self) -> List[str]:
        return list(NETWORK_ACTIONS)

    def specialization(self, role_title: str) -> str:
        return SPECIALIZATION_ACTIONS.get(role_title, SPECIALIZATION_ACTIONS["default"])

    def portfolio(self) -> List[str]:
        return list(PORTFOLIO_ACTIONS)
