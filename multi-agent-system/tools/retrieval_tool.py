def retrieval_tool(question: str):

    print("RETRIEVAL TOOL")

    with open(
        "data/documents.txt",
        "r"
    ) as file:

        content = file.read()

    chunks = content.split("\n\n")

    for chunk in chunks:

        first_word = chunk.split()[0].lower()

        if first_word in question.lower():

            return {
                "document": chunk,
                "source": "documents.txt"
            }

    return {
        "document": "No matching document found",
        "source": "documents.txt"
    }