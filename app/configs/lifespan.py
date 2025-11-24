from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.configs.ai.llm import create_gemini_llm
from app.configs.logger import logger
from app.database.mongodb import close_db, init_db
from app.database.mongodb_saver import saver_cm
from app.database.redis_saver import init_async_redis_saver
from app.database.sqlite_saver import init_async_sqlite_saver
from app.workflows.graphs.graph import build_graph


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---- Initialize DB ----
    logger.info("🚀 Initializing DB connection…")
    await init_db(app)

    # ---- Initialize MongoSaver ----
    logger.info("🚩 Initializing checkpointer…")
    mongodb_saver = saver_cm.__enter__()
    logger.success("✅ Checkpointer initialized successfully!")
    app.state.mongo_saver = mongodb_saver

    # ---- Initialize SqliteSaver ----
    logger.info("⛁ Initializing SqliteSaver…")
    sqlite_saver = await init_async_sqlite_saver()
    logger.success("✅ SqliteSaver initialized successfully!")
    app.state.sqlite_saver = sqlite_saver

    # ---- Initialize RedisSaver ----
    logger.info("♨️ Initializing ReidsSaver")
    redis_saver = await init_async_redis_saver()
    logger.success("✅ RedisSaver initialized successfully!")
    app.state.redis_saver = redis_saver

    # ---- Initialize LLM ----
    logger.info("🤖 Initializing LLM…")
    llm = create_gemini_llm()
    app.state.llm = llm

    # ---- Initialize LangGraph ----
    logger.info("🦜 Initializing LangGraph…")
    app.state.ask_graph = build_graph(llm, checkpointer=mongodb_saver)

    yield

    logger.info("👋 Shutting down DB…")
    await close_db()
