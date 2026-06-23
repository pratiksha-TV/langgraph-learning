from langgraph.graph import StateGraph
from langgraph.graph import END

from state.agent_state import AgentState

from agents.supervisor import supervisor_agent
from agents.math_agent import math_agent
from agents.research_agent import research_agent

from graphs.router import route_agent


builder = StateGraph(
    AgentState
)

builder.add_node(
    "supervisor",
    supervisor_agent
)

builder.add_node(
    "math",
    math_agent
)

builder.add_node(
    "research",
    research_agent
)

builder.set_entry_point(
    "supervisor"
)

builder.add_conditional_edges(
    "supervisor",
    route_agent,
    {
        "math": "math",
        "research": "research"
    }
)

builder.add_edge(
    "math",
    END
)

builder.add_edge(
    "research",
    END
)

graph = builder.compile()