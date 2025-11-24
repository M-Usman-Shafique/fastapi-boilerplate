import aiosqlite
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver


async def init_async_sqlite_saver():
    sqlite_conn = await aiosqlite.connect("sqlite.db")
    return AsyncSqliteSaver(sqlite_conn)
