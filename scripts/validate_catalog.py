#!/usr/bin/env python3
"""Validate static catalog integrity for CI/local checks."""

from __future__ import annotations

from skilldispatch.core.exceptions import CatalogIntegrityError
from skilldispatch.data.legacy_skill_map import LEGACY_TO_AI_MAP
from skilldispatch.data.role_catalog import ROLE_CATALOG, ROLE_DEMAND


def validate() -> None:
    if not LEGACY_TO_AI_MAP:
        raise CatalogIntegrityError("legacy map empty")
    if not ROLE_CATALOG:
        raise CatalogIntegrityError("role catalog empty")
    missing = [title for title in LEGACY_TO_AI_MAP.values() if title not in ROLE_CATALOG]
    # Fallback synthetic titles are allowed; only warn-like raise if too many unknowns.
    if len(missing) > len(LEGACY_TO_AI_MAP) * 0.5:
        raise CatalogIntegrityError(f"too many unmapped role titles: {len(missing)}")
    for title in ROLE_CATALOG:
        if title not in ROLE_DEMAND:
            raise CatalogIntegrityError(f"missing demand for {title}")
    print("catalog_ok", len(LEGACY_TO_AI_MAP), len(ROLE_CATALOG))


if __name__ == "__main__":
    validate()
