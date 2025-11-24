from app.workflows.schemas.ask import AskState


async def get_ask_node(llm):
    async def ask_node(state: AskState) -> AskState:
        try:
            result = await llm.ainvoke(state["prompt"])
            return {
                "prompt": state["prompt"],
                "response": result.text,
            }
        except Exception as e:
            raise RuntimeError(f"LangGraph LLM node error: {e}") from e

    return ask_node
