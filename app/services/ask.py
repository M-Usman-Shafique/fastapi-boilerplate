from app.configs.exceptions.api_error import ApiError
from app.configs.exceptions.decorators import trycatch
from app.services.base import BaseService
from app.utils.response import api_response
from app.workflows.graphs.graph import run_langgraph


class AskService(BaseService):
    def __init__(self, graph):
        self.graph = graph

    @trycatch
    async def get_ask_service(self, prompt: str):
        prompt = prompt.strip()

        if not prompt:
            raise ApiError(400, "Prompt is required")

        llm_response = await run_langgraph(prompt, self.graph)
        return api_response(
            {
                "data": {"You": prompt, "AI": llm_response},
            }
        )
