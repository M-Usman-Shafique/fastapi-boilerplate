from langgraph.checkpoint.redis.aio import AsyncRedisSaver

from app.configs.settings import get_settings

settings = get_settings()


async def init_async_redis_saver():
    return AsyncRedisSaver(redis_url=settings.REDIS_URL)
