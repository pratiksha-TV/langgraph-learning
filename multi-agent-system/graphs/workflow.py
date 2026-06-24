from langgraph.graph import StateGraph
from langgraph.graph import END

from state.rag_state import AgenticRAGState

from agents.planner_agent import planner_agent
from agents.retriever_agent import retriever_agent
from agents.validator_agent import validator_agent

from graphs.router import route_after_planner
from agents.approval_agent import approval_agent
from langgraph.checkpoint.memory import MemorySaver


builder = StateGraph(
    AgenticRAGState
)

builder.add_node(
    "planner",
    planner_agent
)

builder.add_node(
    "retriever",
    retriever_agent
)

builder.add_node(
    "validator",
    validator_agent
)

builder.add_node(
    "approval",
    approval_agent
)

builder.set_entry_point(
    "planner"
)

builder.add_conditional_edges(
    "planner",
    route_after_planner,
    {
        "retriever": "retriever",
        "validator": "validator"
    }
)

builder.add_edge(
    "retriever",
    "validator"
)

builder.add_edge(
    "validator",
    "approval"
)

builder.add_edge(
    "approval",
    END
)

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)