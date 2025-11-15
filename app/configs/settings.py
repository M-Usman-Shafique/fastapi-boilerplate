import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV = os.getenv("ENV", "dev")

class Settings(BaseSettings):
    APP_ENV: str
    APP_NAME: str
    DEBUG: bool
    MONGODB_URI: str
    MONGODB_DB: str

    model_config = SettingsConfigDict(env_file=f".env.{ENV}", case_sensitive=True)


@lru_cache
def get_settings() -> Settings:
    return Settings()  # pyright: ignore[reportCallIssue]
