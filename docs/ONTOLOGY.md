# Ontology Guide

Skilldispatch’s overnight MVP uses curated static dictionaries as a scaffold for a future retrieval + LLM stack.

## Layers

1. **Canonical legacy skills** (`data/legacy_skill_map.py`)
2. **Alias groups** for messy real-world labels
3. **Role catalog** with family/tools/entry metadata
4. **Demand + market signals** for ranking bias
5. **Learning paths** keyed by role family and specialty

## Extending coverage

1. Add a canonical key to `LEGACY_TO_AI_MAP`
2. Optionally add aliases in `SKILL_ALIASES`
3. Ensure the destination role exists in `ROLE_CATALOG`
4. Confirm demand/signal entries exist
5. Run `python scripts/validate_catalog.py`

## Design principle

Coverage breadth beats perfect precision for demos: every common legacy title should return *something* actionable.
