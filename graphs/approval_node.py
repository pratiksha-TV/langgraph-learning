from langgraph.types import interrupt
from state.workflow_state import WorkflowState


def approval_node(state: WorkflowState):

    print("APPROVAL NODE")

    decision = interrupt(
        "Approve this workflow?"
    )

    return {
        "approval": decision
    }

    