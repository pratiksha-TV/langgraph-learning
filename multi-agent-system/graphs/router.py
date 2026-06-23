from state.agent_state import AgentState


def route_agent(state: AgentState):

    if state["agent_type"] == "math":
        return "math"

    return "research"