# NeuroRAG

Production-oriented scaffold for a multi-agent RAG platform built with LangGraph, Ollama, FastAPI, Streamlit, Neon PostgreSQL, pgvector, and Docling.

## Phase 1 Scope

This repository currently includes:

- A single `src` package layout for modular backend, frontend, orchestration, RAG, ingestion, and observability code.
- Typed settings with environment-variable validation.
- Runnable FastAPI backend with health endpoint.
- Runnable Streamlit frontend shell for ingestion and agent output views.
- Smoke tests for health and configuration behavior.

## Tech Stack

- Orchestration: LangGraph
- LLM and Embeddings: Ollama (`llama3`, `nomic-embed-text`)
- Backend API: FastAPI
- Frontend UI: Streamlit
- Database: Neon PostgreSQL + pgvector
- Document Parsing: Docling

## Project Structure

```text
.
├── .env.example
├── pyproject.toml
├── src/
│   └── neurorag/
│       ├── agents/
│       ├── backend/
│       ├── common/
│       ├── config/
│       ├── database/
│       ├── evaluation/
│       ├── frontend/
│       ├── ingestion/
│       ├── observability/
│       ├── orchestration/
│       └── rag/
└── tests/
```

## Prerequisites

- Python 3.11
- `uv` package manager
- Ollama installed locally

## Quick Start

1. Install `uv` if needed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create local environment file:

```bash
cp .env.example .env
```

3. Sync dependencies for Phase 1 (runtime + dev):

```bash
uv sync --group dev
```

4. Optional: install Docling dependencies for Phase 3 ingestion work:

```bash
uv sync --group ingestion
```

5. Pull local Ollama models:

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

6. Run backend API:

```bash
uv run uvicorn neurorag.backend.main:app --host 0.0.0.0 --port 8000 --reload
```

7. Run Streamlit UI in a second terminal:

```bash
uv run streamlit run src/neurorag/frontend/app.py --server.port 8501
```

8. Run smoke tests:

```bash
uv run pytest
```

## Expected Output

- `GET /health` returns JSON with status, service name, version, and environment.
- Streamlit shows ingestion, query, and agent output placeholders.
- Pytest runs and passes health/config smoke checks.

## Environment Variables

See `.env.example` for all fields. Key variables:

- `OLLAMA_BASE_URL`, `OLLAMA_CHAT_MODEL`, `OLLAMA_EMBED_MODEL`
- `NEON_DATABASE_URL`, `REQUIRE_DATABASE`
- `API_HOST`, `API_PORT`, `STREAMLIT_PORT`
- `ENABLE_HITL`, `REQUEST_TIMEOUT_SECONDS`

## Common Errors and Fixes

### 1) `ModuleNotFoundError: neurorag`

Run commands with `uv run ...` from repository root so `src` path settings are applied.

### 2) Missing Ollama models or service unreachable

Start Ollama and pull models:

```bash
ollama serve
ollama pull llama3
ollama pull nomic-embed-text
```

### 3) DB settings error when `REQUIRE_DATABASE=true`

Set `NEON_DATABASE_URL` in `.env` with a valid Neon connection string.

### 4) Port already in use

Change `API_PORT` or `STREAMLIT_PORT` in `.env`, then restart services.

## Next Phase

Phase 2 provisions Neon PostgreSQL and pgvector schema (`documents`, `embeddings`, `query_logs`).