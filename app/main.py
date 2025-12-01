from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.home import router as home
from app.api.routers.registry import routers
from app.configs.constants import origins
from app.configs.exceptions.api_error import ApiError
from app.configs.exceptions.error_handler import (
    api_error_handler,
    http_exception_handler,
    unhandled_exception_handler,
    validation_exception_handler,
)
from app.configs.lifespan import lifespan
from app.configs.settings import get_settings

settings = get_settings()


app = FastAPI(
    title=settings.APP_NAME,
    description="A FastAPI application boilerplate.",
    version="v1",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(ApiError, api_error_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

app.include_router(home)

for router in routers:
    app.include_router(router, prefix="/api")
