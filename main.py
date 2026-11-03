import re
from typing import List, Dict, Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Skillshift MVP")

# --- Data Models ---
class SkillInput(BaseModel):
    skills: str = Field(..., description="Comma-separated legacy skills")
    experience_years: int = Field(..., ge=0, le=50)

class RoadmapStep(BaseModel):
    phase: str
    action: str
    priority: str

class RoadmapResponse(BaseModel):
    original_skills: List[str]
    target_roles: List[str]
    roadmap: List[RoadmapStep]
    estimated_time_weeks: int

# --- Logic: Mock LLM & Market Data ---
# In a real app, this calls a local LLM and a labor API.
LEGACY_TO_AI_MAP = {
    "data entry": "Data Annotation & Labeling",
    "manual testing": "AI Testing Automation",
    "basic accounting": "Financial AI Analysis",
    "customer support": "AI Chatbot Operations",
    "copywriting": "Prompt Engineering"
}

def parse_skills(text: str) -> List[str]:
    return [s.strip().lower() for s in text.split(",") if s.strip()]

def analyze_gaps(skills: List[str], years: int) -> Dict:
    targets = []
    for s in skills:
        if s in LEGACY_TO_AI_MAP:
            targets.append(LEGACY_TO_AI_MAP[s])
        else:
            targets.append(f"AI-adjacent {s.title()}")
    
    # Simple heuristic for roadmap
    steps = []
    if "prompt engineering" in str(targets).lower():
        steps.append(RoadmapStep(phase="1. Foundation", action="Learn LLM constraints", priority="High"))
    else:
        steps.append(RoadmapStep(phase="1. Foundation", action="Learn Python basics", priority="High"))
    
    steps.append(RoadmapStep(phase="2. Practice", action="Build portfolio projects", priority="Medium"))
    steps.append(RoadmapStep(phase="3. Network", action="Join AI communities", priority="Low"))
    
    return {
        "original_skills": skills,
        "target_roles": targets,
        "roadmap": steps,
        "estimated_time_weeks": 12 + (years * 2)
    }

@app.post("/pivot", response_model=RoadmapResponse)
def pivot(input_data: SkillInput):
    if not input_data.skills:
        raise HTTPException(status_code=400, detail="Skills cannot be empty")
    
    skills = parse_skills(input_data.skills)
    if not skills:
        raise HTTPException(status_code=400, detail="No valid skills found")
        
    result = analyze_gaps(skills, input_data.experience_years)
    return result

def demo():
    """CLI Demo for testing without server."""
    test_input = SkillInput(skills="data entry, customer support", experience_years=3)
    res = analyze_gaps(parse_skills(test_input.skills), test_input.experience_years)
    print(f"Original: {res['original_skills']}")
    print(f"Targets: {res['target_roles']}")
    for step in res['roadmap']:
        print(f"  [{step.phase}] {step.action}")
    print(f"Time: {res['estimated_time_weeks']} weeks")

if __name__ == "__main__":
    demo()