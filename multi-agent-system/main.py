from graphs.workflow import graph


question = input(
    "Ask a question: "
)

result = graph.invoke(
    {
        "question": question,
        "agent_type": "",
        "result": ""
    }
)

print("\nFINAL RESULT")
print(result["result"])