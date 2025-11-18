from fastapi import APIRouter, Depends

from app.configs.settings import Settings, get_settings
from app.dependencies.home import get_home_service
from app.services.home import HomeService

router = APIRouter(tags=["home"])


@router.get("/")
async def read_root(
    settings: Settings = Depends(get_settings),
    home_service: HomeService = Depends(get_home_service),
):
    return await home_service.get_message(settings.APP_NAME)
