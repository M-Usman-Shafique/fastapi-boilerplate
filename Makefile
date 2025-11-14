format:
	uv run ruff format .

lint:
	uv run ruff check .

fix:
	uv run ruff check . --fix

typecheck:
	uv run pyright

dev-check:
	uv run ruff format . \
	&& uv run ruff check . \
	&& uv run pyright

dev-server:
	ENV-dev uv run python -m app.main

prod-server:
	ENV=prod uv run python -m app.main
