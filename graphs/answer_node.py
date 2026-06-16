from state.workflow_state import WorkflowState


def answer_node(state: WorkflowState):

    print("ANSWER NODE")

    return {
        "answer": f"Answer: {state['documents']}"
    }