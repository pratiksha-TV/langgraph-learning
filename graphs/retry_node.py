from state.workflow_state import WorkflowState


def retry_node(state: WorkflowState):

    print("RETRY NODE")

    return {
        "retry_count": state["retry_count"] + 1
    }