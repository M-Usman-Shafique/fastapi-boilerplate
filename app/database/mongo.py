from typing import Any

import certifi
from beanie import init_beanie  # type: ignore[attr-defined]
from pymongo import AsyncMongoClient

from app.api.models.registry import doc_models
from app.configs.logger import logger
from app.configs.settings import get_settings

settings = get_settings()

client: AsyncMongoClient[Any] | None = None


async def init_db():
    global client
    if client is None:
        client = AsyncMongoClient(settings.MONGODB_URI, tlsCAFile=certifi.where())

        db = client[settings.MONGODB_DB]

        try:
            await db.command("ping")
            logger.success("✅ DB connected successfully!")
        except Exception as e:
            raise RuntimeError("❌ DB connection failed") from e

        await init_beanie(database=db, document_models=doc_models)


async def close_db():
    global client
    if client is not None:
        await client.close()
        logger.success("⛔ DB disconnected successfully!")
