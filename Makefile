.PHONY: check test validate extract

check: test validate

test:
	python3 -m unittest discover -s tests

validate:
	python3 tools/check_framework.py

extract:
	python3 tools/extract_docx.py --output-dir docs/00_quellen
