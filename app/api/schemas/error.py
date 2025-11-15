from typing import Any

from pydantic import BaseModel


class ErrorResponse(BaseModel):
    success: bool = False
    statusCode: int
    message: str
    data: Any | None = None
    stack: str | None = None
