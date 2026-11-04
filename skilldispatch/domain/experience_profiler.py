"""Convert years-of-experience into pivot velocity hints."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ExperienceProfile:
    years: int
    band: str
    velocity: str
    mentoring_ready: bool


class ExperienceProfiler:
    def profile(self, years: int) -> ExperienceProfile:
        if years <= 1:
            band, velocity, mentoring = "junior", "slow", False
        elif years <= 3:
            band, velocity, mentoring = "early", "moderate", False
        elif years <= 7:
            band, velocity, mentoring = "mid", "fast", True
        elif years <= 15:
            band, velocity, mentoring = "senior", "fast", True
        else:
            band, velocity, mentoring = "principal", "moderate", True
        return ExperienceProfile(
            years=years,
            band=band,
            velocity=velocity,
            mentoring_ready=mentoring,
        )
