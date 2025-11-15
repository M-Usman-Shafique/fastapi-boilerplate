from typing import TypeVar

from app.api.schemas.response import ApiResponse

T = TypeVar("T")


def api_response(
    data: T,
    message: str = "Success",
    status_code: int = 200,
) -> ApiResponse[T]:
    return ApiResponse[T](
        success=status_code < 400,
        statusCode=status_code,
        message=message,
        data=data,
    )
