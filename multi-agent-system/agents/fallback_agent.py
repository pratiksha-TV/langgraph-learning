from state.rag_state import AgenticRAGState


def fallback_agent(state: AgenticRAGState):

    return {
        "answer":
        "Knowledge source unavailable."
    }