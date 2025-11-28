from langgraph.graph import END, StateGraph

from app.workflows.nodes.ask import get_ask_node
from app.workflows.schemas.ask import AskState


async def build_graph(llm, checkpointer):
    workflow = StateGraph[AskState, None, AskState, AskState](AskState)

    ask_node = await get_ask_node(llm)
    workflow.add_node("ask_node", ask_node)
    workflow.set_entry_point("ask_node")
    workflow.add_edge("ask_node", END)

    return workflow.compile(checkpointer=checkpointer)


async def run_langgraph(prompt: str, graph) -> str:
    initial_state: AskState = {"prompt": prompt, "response": None}

    result = await graph.ainvoke(
        initial_state,
        config={"configurable": {"thread_id": "test_thread"}},
    )
    return result["response"]
