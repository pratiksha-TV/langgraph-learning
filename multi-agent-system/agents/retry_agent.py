from state.rag_state import AgenticRAGState

def retry_agent(state: AgenticRAGState):

    print("RETRY AGENT")

    return {
        "retry_count":
        state["retry_count"] + 1,

        "error": ""
    }