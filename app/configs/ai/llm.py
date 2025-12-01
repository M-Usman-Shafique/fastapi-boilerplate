from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from app.configs.constants import (
    DEFAULT_GEMINI_MODEL,
    DEFAULT_GROQ_MODEL,
    DEFAULT_OPENAI_MODEL,
)
from app.configs.settings import get_settings


def create_openai_llm():
    settings = get_settings()
    return ChatOpenAI(
        api_key=settings.OPENAI_API_KEY,
        model=DEFAULT_OPENAI_MODEL,
        temperature=0,
        timeout=None,
        max_retries=2,
    )


def create_gemini_llm():
    settings = get_settings()
    return ChatGoogleGenerativeAI(
        google_api_key=settings.GOOGLE_API_KEY,
        model=DEFAULT_GEMINI_MODEL,
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )


def create_groq_llm():
    settings = get_settings()
    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=DEFAULT_GROQ_MODEL,
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
