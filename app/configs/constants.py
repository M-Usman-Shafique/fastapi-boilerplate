from app.configs.settings import get_settings

settings = get_settings()

origins = [settings.CLIENT_URL]

DEFAULT_GEMINI_MODEL = "gemini-2.5-pro"
DEFAULT_OPENAI_MODEL = "gpt-5-nano"
