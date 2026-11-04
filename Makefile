.PHONY: demo test ontology validate run

demo:
	python scripts/run_demo.py

test:
	pytest -q

ontology:
	python scripts/dump_ontology.py

validate:
	python scripts/validate_catalog.py

run:
	uvicorn main:app --reload
