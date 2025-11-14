from fastapi import FastAPI

from app.api.routers.auth import router as auth_router
from app.api.routers.home import router as home_router
from app.configs.settings import get_settings

settings = get_settings()
app = FastAPI(title=settings.APP_NAME)


app.include_router(home_router)
app.include_router(auth_router)
