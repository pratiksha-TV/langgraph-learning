from state.rag_state import AgenticRAGState


def route_after_planner(
    state: AgenticRAGState
):

    if state["need_retrieval"]:
        return "retriever"

    return "validator"