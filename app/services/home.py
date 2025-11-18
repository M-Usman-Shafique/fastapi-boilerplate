from app.configs.gemini import llm_call
from app.services.base import BaseService
from app.utils.response import api_response


class HomeService(BaseService):
    async def get_message(self, app_name: str):
        prompt = "Hi, there!"
        llm_response = await llm_call(prompt)
        return api_response(
            {
                "message": f"Hello from {app_name}",
                "data": {"user_prompt": prompt, "llm_response": llm_response},
            }
        )
