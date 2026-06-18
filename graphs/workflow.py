from langgraph.graph import StateGraph
from langgraph.graph import END

from state.workflow_state import WorkflowState

from graphs.retrieve_node import retrieve_node
from graphs.answer_node import answer_node
from graphs.retry_node import retry_node
from graphs.router import route_after_retrieve
from langgraph.checkpoint.memory import MemorySaver
from graphs.approval_node import approval_node


builder = StateGraph(
    WorkflowState
)

builder.add_node(
    "retrieve",
    retrieve_node
)

builder.add_node(
    "answer",
    answer_node
)

builder.add_node(
    "retry",
    retry_node
)

builder.add_node(
    "approval",
    approval_node
)

builder.set_entry_point(
    "retrieve"
)

builder.add_conditional_edges(
    "retrieve",
    route_after_retrieve,
    {
        "retry": "retry",
        "approval": "approval"
    }
)

builder.add_edge(
    "retry",
    "retrieve"
)


builder.add_edge(
    "answer",
    END
)


builder.add_edge(
    "approval",
    "answer"
)
memory = MemorySaver()

graph = builder.compile(checkpointer=memory)