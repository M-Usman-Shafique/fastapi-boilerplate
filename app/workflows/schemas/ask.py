from typing import TypedDict


class AskState(TypedDict):
    prompt: str
    response: str | None
