# FastAPI Production API

This project is a production-style backend service built with FastAPI.
The focus is on correctness, clarity, and long-term maintainability rather than rapid prototyping.

The project is developed incrementally with explicit engineering decisions documented along the way.

---

## Goals

- Clean and explicit API design
- Strong separation of concerns
- Reproducible development environment
- Production-ready defaults from day one

---

## Non-Goals

- No frontend or UI
- No premature optimization
- No microservices or distributed complexity
- No framework magic without understanding

---

## Tech Stack

- Python 3.11
- FastAPI
- Poetry for dependency management

Additional components such as databases, authentication, background tasks, and deployment tooling will be added incrementally.

---

## Project Setup

### Requirements

- Python 3.11
- Poetry

### Install Dependencies

pip install poetry
poetry install

### Activate Virtual Environment
poetry shell

### Development Commands
Code Formatting
poetry run black .

### Linting
poetry run ruff check .


### Verify
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```bash
