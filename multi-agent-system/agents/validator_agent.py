from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3"
)

def validator_agent(state):

    retriever_result = state["retriever_result"]

    web_result = state["web_result"]

    response = llm.invoke(
        f"""
        Answer the question using the information below.

        Question:
        {state["question"]}

        Internal Knowledge:
        {retriever_result}

        External Knowledge:
        {web_result}
        """
    )

    return {
        "answer": response.content
    }