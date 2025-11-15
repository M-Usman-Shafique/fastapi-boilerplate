from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.mongo import close_db, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Initializing DB connection…")
    await init_db()
    yield
    print("👋 Shutting down DB…")
    await close_db()
