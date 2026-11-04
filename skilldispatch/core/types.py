"""Lightweight NewType aliases for readability across layers."""

from __future__ import annotations

from typing import NewType

SkillText = NewType("SkillText", str)
RoleTitle = NewType("RoleTitle", str)
Score = NewType("Score", float)
WeekEstimate = NewType("WeekEstimate", int)
