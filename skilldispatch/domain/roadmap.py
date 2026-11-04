"""Compose phased reskilling roadmaps from ranked role matches."""

from __future__ import annotations

from typing import List

from skilldispatch.config.settings import Settings, get_settings
from skilldispatch.data.learning_paths import (
    FOUNDATION_ACTIONS,
    NETWORK_ACTIONS,
    PORTFOLIO_ACTIONS,
    PRACTICE_ACTIONS,
    SPECIALIZATION_ACTIONS,
)
from skilldispatch.data.role_catalog import ROLE_CATALOG
from skilldispatch.models.schemas import RoleMatch, RoadmapStep


class RoadmapComposer:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()

    def _family_for(self, role_title: str) -> str:
        return str(ROLE_CATALOG.get(role_title, {}).get("family", "general"))

    def _hours_for_priority(self, priority: str) -> int:
        return {
            self.settings.default_priority_high: 16,
            self.settings.default_priority_medium: 10,
            self.settings.default_priority_low: 6,
        }.get(priority, 8)

    def compose(self, matches: List[RoleMatch], years: int) -> List[RoadmapStep]:
        if not matches:
            return [
                RoadmapStep(
                    phase=self.settings.foundation_phase_label,
                    action="Learn Python basics and prompt hygiene for knowledge work",
                    priority=self.settings.default_priority_high,
                    estimated_hours=16,
                    skill_focus="general",
                    success_signal="Completed intro notebook + prompt journal",
                )
            ]

        primary = matches[0]
        family = self._family_for(primary.title)
        steps: List[RoadmapStep] = []

        foundation = FOUNDATION_ACTIONS.get(family, FOUNDATION_ACTIONS["general"])
        if "prompt engineering" in primary.title.lower():
            foundation = "Learn LLM constraints, eval harnesses, and prompt contracts"
        steps.append(
            RoadmapStep(
                phase=self.settings.foundation_phase_label,
                action=foundation,
                priority=self.settings.default_priority_high,
                estimated_hours=self._hours_for_priority(self.settings.default_priority_high),
                skill_focus=primary.title,
                success_signal="Can explain tradeoffs of the target role to a peer",
            )
        )

        practice = PRACTICE_ACTIONS.get(family, PRACTICE_ACTIONS["general"])
        steps.append(
            RoadmapStep(
                phase=self.settings.practice_phase_label,
                action=practice if years >= 2 else "Build portfolio projects with weekly critique loops",
                priority=self.settings.default_priority_medium,
                estimated_hours=self._hours_for_priority(self.settings.default_priority_medium),
                skill_focus=primary.title,
                success_signal="One public artifact with measurable outcome",
            )
        )

        network = NETWORK_ACTIONS[min(len(matches) - 1, len(NETWORK_ACTIONS) - 1)]
        steps.append(
            RoadmapStep(
                phase=self.settings.network_phase_label,
                action=network,
                priority=self.settings.default_priority_low,
                estimated_hours=self._hours_for_priority(self.settings.default_priority_low),
                skill_focus="network",
                success_signal="Two informed conversations or one community contribution",
            )
        )

        specialization = SPECIALIZATION_ACTIONS.get(
            primary.title,
            SPECIALIZATION_ACTIONS["default"],
        )
        steps.append(
            RoadmapStep(
                phase=self.settings.specialization_phase_label,
                action=specialization,
                priority=self.settings.default_priority_medium,
                estimated_hours=12,
                skill_focus=primary.title,
                success_signal="Can mentor someone through the first two phases",
            )
        )

        for idx, action in enumerate(PORTFOLIO_ACTIONS[:2]):
            steps.append(
                RoadmapStep(
                    phase=self.settings.portfolio_phase_label,
                    action=action,
                    priority=self.settings.default_priority_medium
                    if idx == 0
                    else self.settings.default_priority_low,
                    estimated_hours=8 if idx == 0 else 5,
                    skill_focus="portfolio",
                    success_signal="Hiring-manager-ready narrative of the pivot",
                )
            )

        # Secondary roles get lighter follow-on actions so the roadmap reflects
        # multi-skill inputs without exploding into noise.
        for secondary in matches[1:3]:
            sec_family = self._family_for(secondary.title)
            steps.append(
                RoadmapStep(
                    phase=self.settings.practice_phase_label,
                    action=(
                        f"Optional adjacent track ({secondary.title}): "
                        + PRACTICE_ACTIONS.get(sec_family, PRACTICE_ACTIONS["general"])
                    ),
                    priority=self.settings.default_priority_low,
                    estimated_hours=6,
                    skill_focus=secondary.title,
                    success_signal="Keep or discard based on energy and market signal",
                )
            )

        return steps[: self.settings.max_roadmap_steps]

    def estimate_weeks(self, years: int, steps: List[RoadmapStep]) -> int:
        base = self.settings.min_roadmap_weeks + (
            years * self.settings.weeks_per_experience_year
        )
        # More steps imply slightly longer calendars; high experience compresses a bit.
        step_penalty = max(0, len(steps) - 3) * 1
        compression = 2 if years >= 8 else 0
        return max(self.settings.min_roadmap_weeks, base + step_penalty - compression)
