from state.workflow_state import WorkflowState


def retrieve_node(state: WorkflowState):

    print("RETRIEVE NODE")

    retry_count = state.get("retry_count", 0)

    print("Retry Count:", retry_count)

    if retry_count == 0:

        print("Returning Error")

        return {
            "error": "Retrieval failed"
        }

    print("Returning Documents")

    return {
        "documents": "Spring Boot is a Java framework.",
        "error": ""
    }