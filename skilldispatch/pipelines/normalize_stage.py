"""Pipeline stage: normalize raw skill text."""

from __future__ import annotations

from typing import List

from skilldispatch.domain.normalizer import SkillNormalizer
from skilldispatch.models.schemas import SkillNormalized


class NormalizeStage:
    def __init__(self, normalizer: SkillNormalizer | None = None) -> None:
        self.normalizer = normalizer or SkillNormalizer()

    def run(self, skills_text: str) -> List[SkillNormalized]:
        return self.normalizer.normalize_text(skills_text)
