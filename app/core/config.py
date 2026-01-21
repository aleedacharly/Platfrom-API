from functools import lru_cache
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # Application
    app_name: str = Field(default="Production API")
    environment: str = Field(default="development")

    # API
    api_v1_prefix: str = Field(default="/api/v1")

    # Security
    secret_key: str = Field(..., min_length=32)
    access_token_expire_minutes: int = Field(default=30)

    # Database
    database_url: str = Field(...)

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
