import functools

from beanie.exceptions import CollectionWasNotInitialized
from langchain_core.exceptions import OutputParserException
from pymongo.errors import PyMongoError

from app.configs.exceptions.api_error import ApiError


def trycatch(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        except OutputParserException as e:
            raise ApiError(
                500, "LLM output parsing failed.", data={"error": str(e)}
            ) from e

        except (PyMongoError, CollectionWasNotInitialized) as e:
            raise ApiError(
                500, "Database operation failed.", data={"error": str(e)}
            ) from e

        except ApiError:
            raise

        except Exception as e:
            raise ApiError(
                500, "Unexpected server error.", data={"error": str(e)}
            ) from e

    return wrapper
