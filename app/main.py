from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends

from app.core.config import get_settings, Settings
from app.api.dependencies import get_app_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()

    print(f"Starting application: {settings.app_name}")
    print(f"Environment: {settings.environment}")

    yield

    print("Shutting down application")


def create_application() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        lifespan=lifespan,
    )

    @app.get("/health")
    def health_check(settings: Settings = Depends(get_app_settings)):
        return {
            "status": "ok",
            "app": settings.app_name,
            "environment": settings.environment,
        }

    return app   # ← THIS WAS MISSING


app = create_application()
