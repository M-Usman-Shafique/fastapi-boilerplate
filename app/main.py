from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.api.routers.registry import routers
from app.configs.exceptions.api_error import ApiError
from app.configs.exceptions.error_handler import (
    api_error_handler,
    http_exception_handler,
    unhandled_exception_handler,
    validation_exception_handler,
)
from app.configs.settings import get_settings
from app.database.lifespan import lifespan

settings = get_settings()


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.add_exception_handler(ApiError, api_error_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)


for r in routers:
    app.include_router(r)
