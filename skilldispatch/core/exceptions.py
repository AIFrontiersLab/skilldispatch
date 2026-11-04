"""Typed application exceptions."""

from __future__ import annotations


class SkilldispatchError(Exception):
    """Base error for Skilldispatch."""


class ValidationFailed(SkilldispatchError):
    """Raised when request payload cannot be used by the pipeline."""


class OntologyMiss(SkilldispatchError):
    """Raised when a skill cannot be resolved and fallbacks are disabled."""


class AdapterUnavailable(SkilldispatchError):
    """Raised when an external adapter is offline or misconfigured."""


class CatalogIntegrityError(SkilldispatchError):
    """Raised when static knowledge bases fail integrity checks."""
