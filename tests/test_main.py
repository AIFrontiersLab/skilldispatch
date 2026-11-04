import pytest
from fastapi.testclient import TestClient
from main import app, SkillInput, parse_skills, analyze_gaps

client = TestClient(app)


def test_startup():
    """Verify FastAPI app starts and health check works."""
    response = client.get("/docs")
    assert response.status_code == 200


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["app"] == "Skilldispatch"
    assert data["adapters"]["llm"] is True
    assert "X-Request-ID" in response.headers
    assert "X-Process-Time-Ms" in response.headers


def test_happy_path():
    """Test successful pivot generation."""
    payload = {
        "skills": "data entry, copywriting",
        "experience_years": 5
    }
    response = client.post("/pivot", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "target_roles" in data
    assert len(data["target_roles"]) == 2
    assert data["estimated_time_weeks"] > 0
    assert data["pipeline_version"] == "static-v3"
    assert len(data["roadmap"]) >= 3
    assert len(data["role_matches"]) == 2


def test_alias_expansion():
    payload = {
        "skills": "customer service, microsoft excel",
        "experience_years": 4,
    }
    response = client.post("/pivot", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "AI Chatbot Operations" in data["target_roles"]
    assert "Analytics Automation Specialist" in data["target_roles"]


def test_failure_empty_skills():
    """Test validation error for empty skills."""
    payload = {
        "skills": "",
        "experience_years": 1
    }
    response = client.post("/pivot", json=payload)
    assert response.status_code == 400


def test_failure_invalid_years():
    """Test validation error for negative years."""
    payload = {
        "skills": "coding",
        "experience_years": -1
    }
    response = client.post("/pivot", json=payload)
    assert response.status_code == 422


def test_parse_skills():
    """Test skill parsing logic."""
    assert parse_skills("a, b, c") == ["a", "b", "c"]
    assert parse_skills("  a  , b") == ["a", "b"]
    assert parse_skills("") == []


def test_analyze_gaps_wrapper():
    result = analyze_gaps(["data entry", "manual testing"], 3)
    assert result["original_skills"]
    assert result["target_roles"]
    assert result["estimated_time_weeks"] >= 8


def test_roles_catalog_endpoint():
    response = client.get("/roles?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 5
    assert "title" in data["roles"][0]


def test_ontology_stats():
    response = client.get("/ontology/stats")
    assert response.status_code == 200
    data = response.json()
    assert data["legacy_skills"] > 50
    assert data["catalog_roles"] > 20


def test_role_market_endpoint():
    response = client.get("/roles/Prompt Engineering/market")
    assert response.status_code == 200
    data = response.json()
    assert data["role_title"] == "Prompt Engineering"
    assert "demand_score" in data
