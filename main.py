from graphs.workflow import graph


result = graph.invoke(
    {
        "question": "What is Spring Boot?",
        "documents": "",
        "answer": "",
        "retry_count": 0,
        "error": ""
    }
)

print("\nFINAL RESULT")
print(result)