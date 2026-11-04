# ADR 0002: Stable FastAPI Contract

## Status

Accepted

## Context

Callers and demos should not break when internal package structure expands.

## Decision

Preserve `POST /pivot` request/response essentials and keep `main.py` as a thin compatibility entrypoint.

## Consequences

- Internal refactors stay cheap
- Public docs remain stable
