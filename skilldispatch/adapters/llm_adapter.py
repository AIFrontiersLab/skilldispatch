"""LLM adapter wrapping the offline stub translator."""

from __future__ import annotations

from typing import List

from skilldispatch.adapters.base import AdapterResult
from skilldispatch.services.llm_stub import LocalLLMTranslator


class LLMAdapter:
    name = "llm"

    def __init__(self, translator: LocalLLMTranslator | None = None) -> None:
        self.translator = translator or LocalLLMTranslator()

    def healthcheck(self) -> AdapterResult:
        return AdapterResult(ok=True, data={"mode": "static"}, source=self.name)

    def translate(self, skills: List[str], roles: List[str]) -> AdapterResult:
        result = self.translator.translate_skills(skills, roles)
        return AdapterResult(
            ok=True,
            data={
                "narrative": result.narrative,
                "model_name": result.model_name,
                "used_live_model": result.used_live_model,
            },
            source=self.name,
        )
