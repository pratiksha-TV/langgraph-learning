from langgraph.graph import StateGraph
from langgraph.graph import END
from langgraph.checkpoint.memory import MemorySaver

from state.rag_state import AgenticRAGState

from agents.planner_agent import planner_agent
from agents.retriever_agent import retriever_agent
from agents.validator_agent import validator_agent
from agents.approval_agent import approval_agent
from agents.retry_agent import retry_agent
from agents.fallback_agent import fallback_agent

from graphs.retriever_router import route_after_retriever


builder = StateGraph(
    AgenticRAGState
)

# Nodes
builder.add_node(
    "planner",
    planner_agent
)

builder.add_node(
    "retriever",
    retriever_agent
)

builder.add_node(
    "retry",
    retry_agent
)

builder.add_node(
    "fallback",
    fallback_agent
)

builder.add_node(
    "validator",
    validator_agent
)

builder.add_node(
    "approval",
    approval_agent
)

# Entry Point
builder.set_entry_point(
    "planner"
)

# Planner -> Retriever
builder.add_edge(
    "planner",
    "retriever"
)

# Retriever Routing
builder.add_conditional_edges(
    "retriever",
    route_after_retriever,
    {
        "retry": "retry",
        "fallback": "fallback",
        "validator": "validator"
    }
)

# Retry -> Retriever
builder.add_edge(
    "retry",
    "retriever"
)

# Validator -> Approval
builder.add_edge(
    "validator",
    "approval"
)

# Approval -> END
builder.add_edge(
    "approval",
    END
)

# Fallback -> END
builder.add_edge(
    "fallback",
    END
)

memory = MemorySaver()

graph = builder.compile(
    checkpointer=memory
)