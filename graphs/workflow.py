from langgraph.graph import StateGraph
from langgraph.graph import END

from state.workflow_state import WorkflowState

from graphs.retrieve_node import retrieve_node
from graphs.answer_node import answer_node


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

builder.set_entry_point(
    "retrieve"
)

builder.add_edge(
    "retrieve",
    "answer"
)

builder.add_edge(
    "answer",
    END
)

graph = builder.compile()