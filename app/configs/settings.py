import os
from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV = os.getenv("ENV", "dev")


class Settings(BaseSettings):
    APP_ENV: str
    APP_NAME: str
    DEBUG: bool
    CLIENT_URL: str
    GOOGLE_API_KEY: SecretStr
    OPENAI_API_KEY: SecretStr
    REDIS_URL: str
    MONGODB_URI: str
    DB_NAME: str

    model_config = SettingsConfigDict(env_file=f".env.{ENV}", case_sensitive=True)


@lru_cache
def get_settings() -> Settings:
    return Settings()  # pyright: ignore[reportCallIssue]
