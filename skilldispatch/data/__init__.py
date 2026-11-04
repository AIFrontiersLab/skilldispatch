"""Static knowledge bases used by the MVP scaffold."""

from skilldispatch.data.legacy_skill_map import LEGACY_TO_AI_MAP, SKILL_ALIASES
from skilldispatch.data.role_catalog import ROLE_CATALOG, ROLE_DEMAND
from skilldispatch.data.learning_paths import FOUNDATION_ACTIONS, PRACTICE_ACTIONS
from skilldispatch.data.market_signals import MARKET_SIGNALS_BY_ROLE

__all__ = [
    "LEGACY_TO_AI_MAP",
    "SKILL_ALIASES",
    "ROLE_CATALOG",
    "ROLE_DEMAND",
    "FOUNDATION_ACTIONS",
    "PRACTICE_ACTIONS",
    "MARKET_SIGNALS_BY_ROLE",
]
