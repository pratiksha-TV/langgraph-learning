from langchain_ollama import ChatOllama

from state.rag_state import AgenticRAGState

llm = ChatOllama(
    model="qwen3"
)


def validator_agent(
    state: AgenticRAGState
):

    print("VALIDATOR AGENT")

    documents = state.get(
        "documents",
        ""
    )

    sources = state.get(
        "sources",
        []
    )

    question = state["question"]

    if documents:

        response = llm.invoke(
            f"""
            Answer the question using only the provided context.

            Context:
            {documents}

            Question:
            {question}
            """
        )

        answer = f"""
{response.content}

Sources:
{", ".join(sources)}
"""

    else:

        answer = """
No supporting documents found.
"""

    return {
        "answer": answer
    }