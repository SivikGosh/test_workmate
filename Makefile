.PHONY: check

install:
	pip install -r requirements.txt

check:
	pytest .
	mypy .
	isort . --check-only
	flake8 .
