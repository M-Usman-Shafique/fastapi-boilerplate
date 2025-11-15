from app.services.base import BaseService
from app.utils.response import api_response


class HomeService(BaseService):
    def get_message(self, app_name: str):
        return api_response({"message": f"Hello from {app_name}"})
