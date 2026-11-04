"""Stub LLM translation layer.

The product brief notes that production Skilldispatch should integrate a local
LLM for resume interpretation. This module documents that seam and provides a
deterministic fallback that never leaves the process.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class LLMTranslationResult:
    source_skills: List[str]
    narrative: str
    model_name: str
    used_live_model: bool


class LocalLLMTranslator:
    """No-op translator that paraphrases using templates only."""

    def __init__(self, model_name: str = "static-scaffold-v0") -> None:
        self.model_name = model_name

    def translate_skills(self, skills: List[str], target_roles: List[str]) -> LLMTranslationResult:
        skill_bit = ", ".join(skills[:5]) or "unspecified skills"
        role_bit = ", ".join(target_roles[:3]) or "exploratory AI-adjacent work"
        narrative = (
            f"Based on {skill_bit}, a practical near-term translation is toward "
            f"{role_bit}. Treat this as a deterministic scaffold until a local "
            f"LLM and labor-market API replace the static dictionaries."
        )
        return LLMTranslationResult(
            source_skills=list(skills),
            narrative=narrative,
            model_name=self.model_name,
            used_live_model=False,
        )

    def summarize_roadmap(self, actions: List[str]) -> str:
        if not actions:
            return "No roadmap actions available."
        head = actions[0]
        more = max(0, len(actions) - 1)
        return f"Start with: {head}. Then execute {more} follow-on phases."
