from skilldispatch.repositories.skill_repository import SkillRepository
from skilldispatch.repositories.role_repository import RoleRepository
from skilldispatch.repositories.learning_repository import LearningRepository
from skilldispatch.domain.gap_analyzer import GapAnalyzer
from skilldispatch.domain.experience_profiler import ExperienceProfiler
from skilldispatch.domain.normalizer import SkillNormalizer
from skilldispatch.domain.matcher import RoleMatcher
from skilldispatch.core.events import DomainEvent, EventBus
from skilldispatch.utils.hashing import pivot_cache_key


def test_skill_repository_coverage():
    repo = SkillRepository()
    coverage = repo.coverage()
    assert coverage["canonical_skills"] > 50
    assert repo.map_role("data entry") == "Data Annotation & Labeling"


def test_role_repository_families_and_top():
    repo = RoleRepository()
    assert "data" in repo.families()
    top = repo.top_by_demand(3)
    assert len(top) == 3
    assert "title" in top[0]


def test_learning_repository_defaults():
    repo = LearningRepository()
    assert "Python" in repo.foundation("general") or "prompt" in repo.foundation("general").lower() or "work" in repo.foundation("general").lower()
    assert repo.portfolio()


def test_gap_and_experience_helpers():
    skills = SkillNormalizer().normalize_text("data entry")
    match = RoleMatcher().match_many(skills, 5)[0]
    gap = GapAnalyzer().analyze(skills, match)
    assert gap.role_title == match.title
    profile = ExperienceProfiler().profile(5)
    assert profile.band == "mid"
    assert profile.mentoring_ready is True


def test_event_bus_and_cache_key():
    bus = EventBus()
    seen = []
    bus.subscribe("pivot.requested", lambda e: seen.append(e.name))
    bus.publish(DomainEvent(name="pivot.requested", payload={"n": 1}))
    assert seen == ["pivot.requested"]
    assert pivot_cache_key("Excel", 3) == pivot_cache_key("excel", 3)
