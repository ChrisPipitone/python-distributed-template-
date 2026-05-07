# Distributed System Template

Boilerplate for distributed systems using FastAPI, Celery, and SQLAlchemy.

## Tech Stack

- **API:** FastAPI
- **Background Tasks:** Celery
- **Broker:** Redis
- **Database:** PostgreSQL
- **Migrations:** Alembic
- **Package Manager:** uv
- **Linting/Formatting:** Ruff
- **Static Analysis:** Pyright

## Architecture

### Structure

Monorepo sharing core logic (models, database sessions, configurations) between API and Worker services.

### Data Access

Generic repository pattern to decouple business logic from the ORM.

### Configuration

Type-safe environment management using pydantic-settings.

### Containerization

Multi-stage Docker builds orchestrated via Docker Compose.

## Usage

### Setup

```bash
uv sync
```

### Infrastructure

```bash
docker compose up -d
```

### Local Services

API:

```bash
uv run uvicorn backend.app.main:app --reload
```

Worker:

```bash
uv run celery -A worker.app.main:celery_app worker --loglevel=info
```

### Quality Control

- **Linting:** `uv run ruff check`
- **Typing:** `uv run pyright`
- **Tests:** `uv run pytest`
