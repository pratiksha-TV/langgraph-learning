from langgraph.types import interrupt


def approval_agent(state):

    print("APPROVAL AGENT")

    approval = interrupt(
        state["answer"]
    )

    if approval.lower() != "yes":

        return {
            "answer":
            "Workflow rejected by human."
        }

    return {
        "approval": approval
    }