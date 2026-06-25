from state.rag_state import AgenticRAGState

def route_after_planner(state: AgenticRAGState):

    if state["error"]:

        return "retry"

    if state["need_retrieval"]:
        return ["retriever", "web"]

    return "validator"