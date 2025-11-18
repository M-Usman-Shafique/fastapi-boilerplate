from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.configs.logger import logger
from app.database.mongo import close_db, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Initializing DB connection…")
    await init_db()
    yield
    logger.info("👋 Shutting down DB…")
    await close_db()
