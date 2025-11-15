import traceback
from typing import Any

from fastapi.responses import JSONResponse

from app.api.schemas.error import ErrorResponse
from app.configs.settings import get_settings


def build_error_response(
    status_code: int,
    message: str,
    data: Any | None,
    exc: Exception,
) -> ErrorResponse:
    settings = get_settings()

    error = ErrorResponse(
        statusCode=status_code,
        message=message,
        data=data,
    )

    if settings.APP_ENV != "production":
        error.stack = "".join(
            traceback.format_exception(type(exc), exc, exc.__traceback__)
        )

    return error


def error_json(status_code: int, error: ErrorResponse) -> JSONResponse:
    return JSONResponse(status_code=status_code, content=error.model_dump())
