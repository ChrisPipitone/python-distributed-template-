.PHONY: up down build logs restart ps backend-shell worker-shell db-shell test clean sync lint

export PYTHONDONTWRITEBYTECODE=1

# Docker Management
COMPOSE = docker compose

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

build:
	$(COMPOSE) build

restart:
	$(COMPOSE) restart

ps:
	$(COMPOSE) ps

logs:
	$(COMPOSE) logs -f

# Shell Access
backend-shell:
	$(COMPOSE) exec backend /bin/bash

worker-shell:
	$(COMPOSE) exec worker /bin/bash

db-shell:
	$(COMPOSE) exec db psql -U postgres -d app

# Development & Testing
sync:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run pyright

# Cleanup
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".pyright_cache" -exec rm -rf {} +
	rm -rf .venv
