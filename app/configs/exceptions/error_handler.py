from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError

from app.configs.exceptions.api_error import ApiError
from app.utils.error import build_error_response, error_json


async def api_error_handler(request: Request, exc: Exception):
    assert isinstance(exc, ApiError)

    error = build_error_response(
        status_code=exc.status_code,
        message=exc.message,
        data=exc.data,
        exc=exc,
    )
    return error_json(exc.status_code, error)


async def http_exception_handler(request: Request, exc: Exception):
    assert isinstance(exc, HTTPException)

    error = build_error_response(
        status_code=exc.status_code,
        message=str(exc.detail),
        data=None,
        exc=exc,
    )
    return error_json(exc.status_code, error)


async def validation_exception_handler(request: Request, exc: Exception):
    assert isinstance(exc, RequestValidationError)

    error = build_error_response(
        status_code=422,
        message="Validation error",
        data={"errors": exc.errors()},
        exc=exc,
    )
    return error_json(422, error)


async def unhandled_exception_handler(request: Request, exc: Exception):
    error = build_error_response(
        status_code=500,
        message="Internal server error",
        data=None,
        exc=exc,
    )
    return error_json(500, error)
