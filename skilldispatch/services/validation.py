"""Request validation beyond Pydantic field constraints."""

from __future__ import annotations

from fastapi import HTTPException

from skilldispatch.config.settings import Settings, get_settings
from skilldispatch.domain.normalizer import SkillNormalizer
from skilldispatch.models.schemas import SkillInput


class PivotValidator:
    def __init__(
        self,
        settings: Settings | None = None,
        normalizer: SkillNormalizer | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self.normalizer = normalizer or SkillNormalizer(self.settings)

    def ensure_usable(self, payload: SkillInput) -> None:
        if not payload.skills or not payload.skills.strip():
            raise HTTPException(status_code=400, detail="Skills cannot be empty")
        parsed = self.normalizer.parse_raw(payload.skills)
        if not parsed:
            raise HTTPException(status_code=400, detail="No valid skills found")
        if payload.experience_years < 0 or payload.experience_years > self.settings.max_experience_years:
            raise HTTPException(status_code=400, detail="experience_years out of range")
