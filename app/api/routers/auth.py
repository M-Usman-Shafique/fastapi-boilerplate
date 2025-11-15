from fastapi import APIRouter, Depends

from app.api.dependencies.auth import get_auth_service
from app.api.schemas.user import UserCreate
from app.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup")
async def create_user(
    new_user: UserCreate, auth_service: AuthService = Depends(get_auth_service)
):
    return await auth_service.signup(new_user)
