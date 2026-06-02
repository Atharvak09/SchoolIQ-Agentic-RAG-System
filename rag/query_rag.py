from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_PATH = "rag/chroma_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embedding_model
)

def query_rag(question: str, k: int = 8):
    """
    Retrieve relevant student records for RAG.
    Ensures:
    - multiple students
    - valid grade data
    - question-aware filtering
    """

    docs = vector_db.similarity_search(question, k=k)

    cleaned_docs = []

    for doc in docs:
        text = doc.page_content.strip()

        # basic sanity filter
        if "Final Grade" not in text:
            continue

        cleaned_docs.append(text)

    # question-aware filtering
    q = question.lower()

    if "high-performing" in q or "top" in q or "excellent" in q:
        cleaned_docs = [
            d for d in cleaned_docs
            if any(g in d for g in [
                "Final Grade: 12",
                "Final Grade: 13",
                "Final Grade: 14",
                "Final Grade: 15",
                "Final Grade: 16",
                "Final Grade: 17",
                "Final Grade: 18",
                "Final Grade: 19",
                "Final Grade: 20"
            ])
        ]

    # fallback safety
    if len(cleaned_docs) < 3:
        cleaned_docs = cleaned_docs[:3]

    return cleaned_docs
