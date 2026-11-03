import pytest
from fastapi.testclient import TestClient
from main import app, SkillInput, parse_skills

client = TestClient(app)

def test_startup():
    """Verify FastAPI app starts and health check works."""
    response = client.get("/docs")
    assert response.status_code == 200

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