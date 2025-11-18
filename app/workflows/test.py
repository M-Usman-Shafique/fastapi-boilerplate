from typing import TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph

from app.configs.gemini import llm


class GraphState(TypedDict):
    prompt: str
    response: str | None


async def call_llm(state: GraphState) -> GraphState:
    try:
        result = await llm.ainvoke(state["prompt"])
        return {"prompt": state["prompt"], "response": result.text}
    except Exception as e:
        raise RuntimeError(f"LangGraph LLM node error: {e}") from e


# Build the graph
workflow = StateGraph(GraphState)
workflow.add_node("llm_node", call_llm)

workflow.set_entry_point("llm_node")
workflow.add_edge("llm_node", END)

# In-memory checkpointing
checkpointer = MemorySaver()

graph = workflow.compile(checkpointer=checkpointer)


async def run_langgraph(prompt: str) -> str:
    initial_state: GraphState = {"prompt": prompt, "response": None}

    result = await graph.ainvoke(
        initial_state,
        config={"configurable": {"thread_id": "test_thread"}},
    )
    return result["response"]
