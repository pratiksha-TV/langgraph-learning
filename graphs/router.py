from state.workflow_state import WorkflowState


def route_after_retrieve(
    state: WorkflowState
):

    if state.get("error"):

        return "retry"

    return "approval"