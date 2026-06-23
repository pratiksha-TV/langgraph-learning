from state.workflow_state import WorkflowState


def retry_node(state: WorkflowState):

    print("RETRY NODE")

    retry_count = state.get("retry_count", 0)

    print("Retry Count:", retry_count)

    return {
        "retry_count": retry_count + 1
    }