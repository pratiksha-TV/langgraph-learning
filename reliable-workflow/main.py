from graphs.workflow import graph
from langgraph.types import Command

config = {
    "configurable": {
        "thread_id": "user_1"
    }
}

result = graph.invoke(
    {
        "question": "What is Spring Boot?",
        "documents": "",
        "answer": "",
        "retry_count": 0,
        "error": "",
        "approval": ""
    },
    config=config
)

print(result)

if "__interrupt__" in result:

    approval = input(
        "\nApprove workflow? (yes/no): "
    )

    result = graph.invoke(
        Command(resume=approval),
        config=config
    )

    print("\nFINAL RESULT")
    print(result)