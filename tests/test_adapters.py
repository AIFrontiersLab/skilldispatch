from skilldispatch.adapters.llm_adapter import LLMAdapter
from skilldispatch.adapters.labor_adapter import LaborMarketAdapter
from skilldispatch.adapters.storage_adapter import InMemoryStorageAdapter
from skilldispatch.services.health import HealthService
from skilldispatch.services.report_builder import ReportBuilder
from skilldispatch.models.schemas import SkillInput
from skilldispatch.services.orchestrator import SkillDispatchOrchestrator


def test_llm_adapter_health_and_translate():
    adapter = LLMAdapter()
    assert adapter.healthcheck().ok
    result = adapter.translate(["excel"], ["Analytics Automation Specialist"])
    assert result.ok
    assert "Analytics Automation Specialist" in result.data["narrative"]


def test_labor_adapter_observe():
    adapter = LaborMarketAdapter()
    assert adapter.healthcheck().ok
    result = adapter.observe("Prompt Engineering")
    assert result.ok
    assert result.data["role_title"] == "Prompt Engineering"


def test_storage_adapter_roundtrip():
    storage = InMemoryStorageAdapter()
    saved = storage.save({"hello": "world"})
    assert saved.ok
    loaded = storage.get(saved.data["id"])
    assert loaded.ok
    assert loaded.data["hello"] == "world"


def test_health_service_reports_adapters():
    status = HealthService().status()
    assert status["status"] == "ok"
    assert status["adapters"]["llm"] is True


def test_report_builder_markdown():
    result = SkillDispatchOrchestrator().pivot(
        SkillInput(skills="data entry, copywriting", experience_years=4)
    )
    md = ReportBuilder().build_markdown(result)
    assert "# Skilldispatch Pivot Report" in md
    assert "Target Roles" in md
