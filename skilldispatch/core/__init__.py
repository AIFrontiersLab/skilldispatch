"""Core primitives: constants, exceptions, types, and domain events."""

from skilldispatch.core.constants import PIPELINE_VERSION, DEFAULT_LOCALE
from skilldispatch.core.exceptions import SkilldispatchError, ValidationFailed, OntologyMiss
from skilldispatch.core.types import SkillText, RoleTitle, Score
from skilldispatch.core.events import DomainEvent, EventBus

__all__ = [
    "PIPELINE_VERSION",
    "DEFAULT_LOCALE",
    "SkilldispatchError",
    "ValidationFailed",
    "OntologyMiss",
    "SkillText",
    "RoleTitle",
    "Score",
    "DomainEvent",
    "EventBus",
]
