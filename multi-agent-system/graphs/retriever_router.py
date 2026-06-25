from state.rag_state import AgenticRAGState

def route_after_retriever(state: AgenticRAGState):

    if state.get("error"):

        if state["retry_count"] >= 3:
            return "fallback"

        return "retry"

    return "validator"