from graphs.workflow import graph
from langgraph.types import Command



question = input(
    "Ask a question: "
)

result = graph.invoke(
    {
        "question": question,
        "retry_count": 0,
        "error": "",
        "need_retrieval": False,
        "retriever_result": "",
        "web_result": "",
        "answer": "",
        "sources": [],
        "approval": ""
    },
    config={
        "configurable": {
            "thread_id": "user_1"
        }
    }
)
if "__interrupt__" in result:

    approval = input(
        "\nApprove answer? (yes/no): "
    )

    result = graph.invoke(
        Command(
            resume=approval
        ),
        config={
            "configurable": {
                "thread_id": "user_1"
            }
        }
    )

    print("\nFINAL RESULT")
    print(result)

print("\nFINAL RESULT")
print(result)