from rag.query_rag import query_rag

def retrieve_context(question: str):
    docs = query_rag(question)
    return "\n\n".join(docs)
