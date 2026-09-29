.PHONY: check extract

check:
	python3 tools/check_framework.py

extract:
	python3 tools/extract_docx.py --output-dir docs/00_quellen
