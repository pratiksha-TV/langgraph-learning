from graphs.retrieve_node import retrieve_node
from graphs.answer_node import answer_node


state = {
    "question": "What is Spring Boot?",
    "documents": "",
    "answer": "",
    "retry_count": 0,
    "error": ""
}

print("INITIAL STATE")
print(state)

retrieve_result = retrieve_node(state)

state.update(retrieve_result)

answer_result = answer_node(state)

state.update(answer_result)

print("\nFINAL STATE")
print(state)