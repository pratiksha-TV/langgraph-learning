from state.agent_state import AgentState


def math_agent(state: AgentState):

    print("MATH AGENT")

    question = state["question"]

    numbers = question.replace("?", "").split("+")

    result = int(numbers[0].split()[-1]) + int(numbers[1])

    return {
        "result": str(result)
    }