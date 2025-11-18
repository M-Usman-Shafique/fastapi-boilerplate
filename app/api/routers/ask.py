from fastapi import APIRouter, Depends

from app.api.models.ask import AskRequest
from app.dependencies.ask import get_ask_service
from app.services.ask import AskService

router = APIRouter(prefix="/ask", tags=["ask"])


@router.post("")
async def ask(
    body: AskRequest,
    ask_service: AskService = Depends(get_ask_service),
):
    return await ask_service.get_ask_service(body.prompt)
