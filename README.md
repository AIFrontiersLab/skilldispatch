# Skilldispatch

Translate legacy technical skills into actionable, high-demand AI-adjacent career paths

# Skillshift MVP

Translates legacy technical skills into actionable, high-demand AI-adjacent career paths.

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Run the server:
   uvicorn main:app --reload

3. API Endpoint:
   POST /pivot
   Body: { "skills": "data entry, customer support", "experience_years": 3 }

## Demo

Run the CLI demo:
   python -c "from main import demo; demo()"

## Tests

   pytest -q