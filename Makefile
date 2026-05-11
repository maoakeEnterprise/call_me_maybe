SRC = src/__main__.py

PARSING = utils/parsing.py

run:
	@uv run python -m src

install:
	uv sync

test_parsing:
	uv run pytest tests/test_parsing.py

norming:
	watch flake8 $(SRC) $(PARSING)