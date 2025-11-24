from fastapi import Request

from app.services.ask import AskService


def get_ask_service(request: Request):
    graph = request.app.state.ask_graph
    return AskService(graph)
