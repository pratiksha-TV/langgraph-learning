from state.agent_state import AgentState


def supervisor_agent(state: AgentState):

    print("SUPERVISOR AGENT")

    question = state["question"].lower()

    if "+" in question:
        return {
            "agent_type": "math"
        }

    return {
        "agent_type": "research"
    }