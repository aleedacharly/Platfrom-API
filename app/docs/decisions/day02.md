# Day 02 – Application Control and Dependency Injection

## Goal

Establish explicit control over application behavior, configuration, and dependencies.

Day 02 focuses on correctness and extensibility rather than features.

---

## Configuration Management

A centralized configuration system is implemented using Pydantic Settings.
Environment variables are the single source of truth.

The application fails fast if required configuration is missing.

---

## Application Lifespan

Startup and shutdown behavior is explicitly defined using FastAPI’s lifespan mechanism.
This prevents side effects at import time and prepares the system for resource management.

---

## Dependency Injection

FastAPI’s dependency injection system is introduced for application settings.
Routes declare required dependencies instead of accessing global state.

This enables testing, extensibility, and future infrastructure integration.

---

## Outcome

By the end of Day 02:
- Application startup and shutdown are deterministic
- Configuration is validated and explicit
- Dependencies are injectable and testable
- The system is ready for database integration
