from skilldispatch.config.settings import Settings
from skilldispatch.domain.normalizer import SkillNormalizer
from skilldispatch.domain.matcher import RoleMatcher
from skilldispatch.domain.roadmap import RoadmapComposer
from skilldispatch.domain.scoring import ScoreEngine
from skilldispatch.models.schemas import SkillInput
from skilldispatch.pipelines.pivot_pipeline import PivotPipeline
from skilldispatch.services.llm_stub import LocalLLMTranslator
from skilldispatch.services.labor_market_stub import LaborMarketClient


def test_normalizer_dedupes_and_aliases():
    n = SkillNormalizer()
    skills = n.normalize_text("Data Entry, data-entry, CUSTOMER SERVICE")
    canonicals = [s.canonical for s in skills]
    assert "data entry" in canonicals
    assert "customer support" in canonicals
    assert len(canonicals) == 2


def test_score_engine_bands():
    engine = ScoreEngine()
    assert engine.confidence_band(0.9).value == "immediate"
    assert engine.confidence_band(0.75).value == "strong"
    assert engine.confidence_band(0.6).value == "promising"
    assert engine.confidence_band(0.4).value == "exploratory"


def test_matcher_ranks_known_skills_above_unknown():
    settings = Settings()
    matcher = RoleMatcher(settings)
    normalizer = SkillNormalizer(settings)
    known = normalizer.normalize_text("prompt-ish-not-real, copywriting")
    # Force one unknown + one known through matcher
    matches = matcher.match_many(known, years=5)
    assert matches
    assert matches[0].composite_score >= matches[-1].composite_score


def test_roadmap_respects_max_steps():
    settings = Settings(max_roadmap_steps=4)
    composer = RoadmapComposer(settings)
    matcher = RoleMatcher(settings)
    skills = SkillNormalizer(settings).normalize_text(
        "data entry, sql, compliance, recruiting, excel"
    )
    matches = matcher.match_many(skills, years=6)
    steps = composer.compose(matches, years=6)
    assert len(steps) <= 4


def test_pipeline_end_to_end():
    pipeline = PivotPipeline()
    result = pipeline.run(
        SkillInput(skills="bookkeeping, help desk, sql", experience_years=7)
    )
    assert len(result.target_roles) >= 2
    assert result.estimated_time_weeks >= 8
    assert "skills_in" in result.diagnostics


def test_llm_and_labor_stubs():
    llm = LocalLLMTranslator()
    translated = llm.translate_skills(["excel"], ["Analytics Automation Specialist"])
    assert translated.used_live_model is False
    assert "Analytics Automation Specialist" in translated.narrative

    labor = LaborMarketClient()
    top = labor.top_demand(3)
    assert len(top) == 3
    assert labor.explain(top[0].role_title)
