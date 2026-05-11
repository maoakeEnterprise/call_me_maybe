SRC = src/__main__.py

PARSING = utils/parsing.py

TESTS = tests/test_parsing.py

run:
	@uv run python -m src

install:
	uv sync

test_parsing:
	uv run pytest tests/test_parsing.py

norming:
	watch flake8 $(SRC) $(PARSING) $(TESTS)

lint:
	uv run flake8 . --exclude=.venv --exclude=llm_sdk
	uv run mypy .  --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs