SRC = src/__main__.py

PARSING = utils/parsing.py

run:
	@uv run python -m src

install:
	uv sync

norming:
	watch flake8 $(SRC) $(PARSING)