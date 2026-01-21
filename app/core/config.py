from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "Production API"
    environment: str = "development"

    api_v1_prefix: str = "/api/v1"

    secret_key: str = Field(..., validation_alias="SECRET_KEY")
    access_token_expire_minutes: int = 30

    database_url: str = Field(..., validation_alias="DATABASE_URL")


@lru_cache
def get_settings() -> Settings:
    return Settings()
