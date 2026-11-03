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

## Architecture

![Architecture](docs/architecture.png)

<details>
<summary>Mermaid source</summary>

```mermaid
flowchart LR
    A[User Input] --> B[FastAPI Server]
    B --> C[Parse Skills]
    C --> D[Map to AI Roles]
    D --> E[Generate Roadmap]
    E --> F[JSON Response]
```

</details>
