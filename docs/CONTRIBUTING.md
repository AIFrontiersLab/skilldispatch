# Contributing

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Project conventions

- Keep `POST /pivot` backward compatible
- Prefer deterministic static behavior in MVP modes
- Put outbound integrations behind adapters
- Add tests for parser/ranking changes
- Update docs when endpoints or package layout change

## Useful commands

```bash
python scripts/run_demo.py
python scripts/dump_ontology.py
python scripts/validate_catalog.py
python -m skilldispatch.cli pivot --skills "excel, sql" --years 5
```
