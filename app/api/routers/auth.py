from fastapi import APIRouter, Depends

from app.api.dependencies.auth import get_auth_service
from app.services.auth import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/")
def login( auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.login()
