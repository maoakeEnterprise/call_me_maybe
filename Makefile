SRC = src/__main__.py

UTILS = utils/parsing.py utils/input.py utils/translator.py

TESTS = tests/test_parsing.py

run:
	@uv run python -m src

install:
	uv sync

test_parsing:
	uv run pytest tests/test_parsing.py

norming:
	watch flake8 $(SRC) $(UTILS) $(TESTS)

norming-mypy:
	watch uv run mypy $(SRC) $(UTILS) $(TESTS) --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint:
# 	uv run flake8 . --exclude=./.venv,./llm_sdk
	uv run mypy . --exclude=./.venv,./llm_sdk --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs