from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.api.routers.auth import router as auth_router
from app.api.routers.home import router as home_router
from app.configs.exceptions.api_error import ApiError
from app.configs.exceptions.error_handler import (
    api_error_handler,
    http_exception_handler,
    unhandled_exception_handler,
    validation_exception_handler,
)
from app.configs.settings import get_settings

settings = get_settings()
app = FastAPI(title=settings.APP_NAME)

app.add_exception_handler(ApiError, api_error_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)


app.include_router(home_router)
app.include_router(auth_router)
