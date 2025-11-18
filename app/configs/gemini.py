from google import genai

from app.configs.constants import DEFAULT_MODEL
from app.configs.settings import get_settings

settings = get_settings()

client = genai.Client(api_key=settings.GOOGLE_API_KEY)


def llm_call(prompt: str, model: str = DEFAULT_MODEL) -> str | None:
    try:
        response = client.models.generate_content(  # type: ignore[reportUnknownMemberType]
            model=model,
            contents=prompt,
        )
        return response.text

    except Exception as e:
        raise RuntimeError(f"Gemini client error: {e}") from e
