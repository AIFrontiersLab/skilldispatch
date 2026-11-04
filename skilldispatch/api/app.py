"""FastAPI application factory."""

from __future__ import annotations

from fastapi import FastAPI

from skilldispatch.api.routes import router
from skilldispatch.config.settings import get_settings
from skilldispatch.middleware.request_context import RequestContextMiddleware
from skilldispatch.middleware.timing import TimingMiddleware


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=f"{settings.app_name} MVP",
        description=(
            "Deterministic legacy-skill → AI-adjacent roadmap translator. "
            "Static dictionaries scaffold a future local-LLM + labor-market stack."
        ),
        version=settings.api_version,
    )
    app.add_middleware(TimingMiddleware)
    app.add_middleware(RequestContextMiddleware)
    app.include_router(router)
    return app
