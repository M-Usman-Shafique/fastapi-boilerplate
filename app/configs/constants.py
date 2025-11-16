from app.configs.settings import get_settings

settings = get_settings()

origins = [settings.CLIENT_URL]
