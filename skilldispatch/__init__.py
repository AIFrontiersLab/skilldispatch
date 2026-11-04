"""Skilldispatch — legacy skill translation into AI-adjacent career infrastructure.

This package implements a multi-stage deterministic pipeline that:

1. Normalizes and tokenizes free-form skill input
2. Resolves aliases against a curated legacy-skill ontology
3. Scores adjacency to AI-era roles using weighted taxonomies
4. Composes phased reskilling roadmaps with effort heuristics
5. Emits structured API responses suitable for portfolio tooling

The current MVP uses static dictionaries as a scaffold. Production
deployments are expected to swap the static layers for local LLM
inference and live labor-market feeds without changing the public
FastAPI contract.
"""

from skilldispatch.config.settings import Settings, get_settings
from skilldispatch.services.orchestrator import SkillDispatchOrchestrator

__all__ = [
    "Settings",
    "get_settings",
    "SkillDispatchOrchestrator",
    "__version__",
]

__version__ = "0.3.0"
