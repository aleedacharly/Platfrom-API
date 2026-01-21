from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()

    # Startup logic
    print(f"Starting application: {settings.app_name}")
    print(f"Environment: {settings.environment}")

    yield

    # Shutdown logic
    print("Shutting down application")


def create_application() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        lifespan=lifespan,
    )

    @app.get("/health")
    def health_check():
        return {"status": "ok"}

    return app


app = create_application()
