from langgraph.graph import StateGraph
from langgraph.graph import END

from state.workflow_state import WorkflowState

from graphs.retrieve_node import retrieve_node
from graphs.answer_node import answer_node
from graphs.retry_node import retry_node
from graphs.router import route_after_retrieve


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

builder.set_entry_point(
    "retrieve"
)

builder.add_conditional_edges(
    "retrieve",
    route_after_retrieve,
    {
        "retry": "retry",
        "answer": "answer"
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

graph = builder.compile()