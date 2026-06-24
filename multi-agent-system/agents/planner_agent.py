from state.rag_state import AgenticRAGState


def planner_agent(state: AgenticRAGState):

    print("PLANNER AGENT")

    question = state["question"].lower()

    math_keywords = [
        "+",
        "-",
        "*",
        "/"
    ]

    need_retrieval = True

    for keyword in math_keywords:
        if keyword in question:
            need_retrieval = False
            break

    return {
        "need_retrieval": need_retrieval
    }
    