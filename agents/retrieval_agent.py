from utils.vector_store import load_vectorstore


def retrieve_context(query):
    vectorstore = load_vectorstore()

    if vectorstore is None:
        return "No document indexed yet."

    docs = vectorstore.similarity_search(query, k=4)

    context = "\n\n".join([doc.page_content for doc in docs])

    # 🔥 DEBUG LINE (STEP 4)
    print("Retrieved context:", context)

    return context
