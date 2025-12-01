from app.configs.settings import get_settings

settings = get_settings()

origins = [settings.CLIENT_URL]

DEFAULT_OPENAI_MODEL = "gpt-5-nano"
DEFAULT_GEMINI_MODEL = "gemini-2.5-pro"
DEFAULT_GROQ_MODEL = "llama-3.1-8b-instant"
