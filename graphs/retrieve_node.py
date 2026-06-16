def retrieve_node(state):

    print("RETRIEVE NODE")
    print("Retry Count:", state["retry_count"])

    if state["retry_count"] == 0:

        print("Returning Error")

        return {
            "error": "Retrieval failed"
        }

    print("Returning Documents")

    return {
        "documents": "Spring Boot is a Java framework.",
        "error": ""
    }