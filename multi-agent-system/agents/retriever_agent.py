from state.rag_state import AgenticRAGState

from tools.retrieval_tool import (
    retrieval_tool
)


def retriever_agent(
    state: AgenticRAGState
):

    print("RETRIEVER AGENT")

    result = retrieval_tool(
        state["question"]
    )

    return {
        "documents":
            result["document"],

        "sources":
            [result["source"]]
    }