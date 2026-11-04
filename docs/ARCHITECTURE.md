# Skilldispatch Architecture

## Overview

Skilldispatch is a multi-stage career-translation service. The public contract is intentionally small (`POST /pivot`) while the internal package is staged so each concern can be replaced independently:

| Stage | Module | Responsibility | Replaceability |
| --- | --- | --- | --- |
| Ingest | `domain.normalizer` | tokenize, alias, categorize | swap for resume PDF/OCR parser |
| Score | `domain.scoring` | adjacency / demand / experience blend | swap weights via settings |
| Match | `domain.matcher` | role ranking + rationales | swap for embedding retrieval |
| Plan | `domain.roadmap` | phased actions + week estimate | swap for LLM planner |
| Serve | `api.routes` | HTTP surface | keep stable |
| Observe | `services.telemetry` | event sink | swap for OpenTelemetry |

## Data plane

The overnight MVP stores four static knowledge bases under `skilldispatch/data/`:

1. **legacy_skill_map** — canonical legacy skill → AI-adjacent role titles, plus alias groups
2. **role_catalog** — role metadata (family, tools, entry barrier, remote friendliness)
3. **learning_paths** — foundation / practice / network / specialization / portfolio actions
4. **market_signals** — synthetic demand/obsolescence hints until a live labor API exists

## Control plane

`Settings` centralizes thresholds (max roles, confidence bands, week heuristics, feature flags). Feature flags currently gate:

- alias expansion
- adjacency scoring
- market-demand bias
- confidence-band labeling

## Future adapters

### Local LLM

`services.llm_stub.LocalLLMTranslator` is the seam. A production adapter should:

1. Accept normalized skills + optional resume text
2. Emit structured role hypotheses with citations
3. Fail soft back to the static ontology when the model is offline

### Labor market API

`services.labor_market_stub.LaborMarketClient` is the seam. A production adapter should:

1. Fetch demand / wage / posting velocity by role and geography
2. Cache observations aggressively
3. Preserve the `LaborMarketObservation` dataclass shape used by diagnostics

## Runtime topology

```text
uvicorn main:app
  └─ create_app()
       └─ APIRouter
            ├─ /health
            ├─ /pivot
            ├─ /roles
            ├─ /roles/{title}/market
            └─ /ontology/stats
```

CLI demos call the same orchestrator without starting HTTP.

## Testing strategy

- API contract tests in `tests/test_main.py`
- Domain/pipeline unit tests in `tests/test_pipeline.py`
- Prefer deterministic fixtures over networked fixtures
