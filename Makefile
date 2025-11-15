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

pre-commit-install:
	uv run pre-commit install --install-hooks

dev-start:
	echo "Starting in DEV mode"
	ENV=dev uv run uvicorn app.main:app \
		--loop uvloop \
		--http httptools \
		--host 0.0.0.0 \
		--port 8000

dev-run:
	echo "Starting in DEV mode (auto-reload)"
	ENV=dev uv run uvicorn app.main:app \
		--reload \
		--loop uvloop \
		--http httptools \
		--host 0.0.0.0 \
		--port 8000

prod-start:
	echo "Starting in PROD mode"
	ENV=prod uv run uvicorn app.main:app \
		--loop uvloop \
		--http httptools \
		--host 0.0.0.0 \
		--port 8000
