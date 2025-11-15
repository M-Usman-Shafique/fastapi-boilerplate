
from app.services.base import BaseService


class HomeService(BaseService):

    def get_message(self, app_name: str):
        return {"message": f"Hello from {app_name}"}
