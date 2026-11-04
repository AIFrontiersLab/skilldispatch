"""CLI command implementations."""

from __future__ import annotations

import json

from skilldispatch.models.schemas import SkillInput
from skilldispatch.repositories.skill_repository import SkillRepository
from skilldispatch.repositories.role_repository import RoleRepository
from skilldispatch.services.orchestrator import SkillDispatchOrchestrator


def cmd_demo(_args) -> int:
    from main import demo

    demo()
    return 0


def cmd_pivot(args) -> int:
    orch = SkillDispatchOrchestrator()
    result = orch.pivot(SkillInput(skills=args.skills, experience_years=args.years))
    print(json.dumps(result.model_dump(), indent=2))
    return 0


def cmd_dump_ontology(_args) -> int:
    skills = SkillRepository().coverage()
    roles = RoleRepository()
    payload = {
        "skills": skills,
        "families": roles.families(),
        "top_roles": roles.top_by_demand(5),
    }
    print(json.dumps(payload, indent=2))
    return 0
