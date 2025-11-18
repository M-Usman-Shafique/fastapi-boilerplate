from app.services.base import BaseService
from app.utils.response import api_response
from app.workflows.test import run_langgraph


class AskService(BaseService):
    async def get_ask_service(self, prompt: str):
        llm_response = await run_langgraph(prompt)
        return api_response(
            {
                "data": {"You": prompt, "AI": llm_response},
            }
        )
