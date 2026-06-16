from graphs.retrieve_node import retrieve_node


result = retrieve_node(
    {
        "question": "What is Spring Boot?",
        "documents": "",
        "answer": "",
        "retry_count": 0,
        "error": ""
    }
)

print(result)