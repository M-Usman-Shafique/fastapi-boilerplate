from fastapi import APIRouter, Depends

from app.configs.settings import Settings, get_settings

router = APIRouter(tags=["home"])


@router.get("/")
def read_root(settings: Settings=Depends(get_settings)):
    return {"message": f"Hello from {settings.APP_NAME}"}
