from langchain_ollama import ChatOllama

from state.agent_state import AgentState


llm = ChatOllama(
    model="qwen3"
)


def supervisor_agent(state: AgentState):

    print("SUPERVISOR AGENT")

    question = state["question"]

    response = llm.invoke(
        f"""
        You are a supervisor agent.

        Available agents:

        1. math
        - calculations
        - arithmetic
        - numbers

        2. research
        - general knowledge
        - explanations
        - concepts

        Question:
        {question}

        Return only:
        math
        or
        research
        """
    )

    selected_agent = (
        response.content
        .strip()
        .lower()
    )

    print(
        "Selected Agent:",
        selected_agent
    )

    return {
        "agent_type": selected_agent
    }