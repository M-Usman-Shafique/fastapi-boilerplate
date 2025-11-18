from langchain_google_genai import ChatGoogleGenerativeAI

from app.configs.constants import DEFAULT_MODEL
from app.configs.settings import get_settings

settings = get_settings()

llm = ChatGoogleGenerativeAI(
    google_api_key=settings.GOOGLE_API_KEY,
    model=DEFAULT_MODEL,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)
