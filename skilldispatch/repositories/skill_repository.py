"""Repository for legacy skill ontology lookups."""

from __future__ import annotations

from typing import Dict, List, Optional

from skilldispatch.data.legacy_skill_map import LEGACY_TO_AI_MAP, SKILL_ALIASES


class SkillRepository:
    def map_role(self, skill: str) -> Optional[str]:
        return LEGACY_TO_AI_MAP.get(skill)

    def aliases_for(self, skill: str) -> List[str]:
        return list(SKILL_ALIASES.get(skill, []))

    def all_canonical_skills(self) -> List[str]:
        return sorted(LEGACY_TO_AI_MAP.keys())

    def coverage(self) -> Dict[str, int]:
        return {
            "canonical_skills": len(LEGACY_TO_AI_MAP),
            "alias_groups": len(SKILL_ALIASES),
            "alias_terms": sum(len(v) for v in SKILL_ALIASES.values()),
        }
