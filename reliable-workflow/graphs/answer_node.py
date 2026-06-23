from state.workflow_state import WorkflowState


def answer_node(state):

    print("ANSWER NODE")

    if state['approval'] != "yes":

        return {
            "answer": "Workflow rejected by human."
        }

    return {
        "answer":
        f"""
        Approval: {state['approval']}
        Context: {state['documents']}
        """
    }