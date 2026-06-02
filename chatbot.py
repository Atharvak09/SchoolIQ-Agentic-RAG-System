from router.question_router import classify_question_llm
from llm.sql_generator import generate_sql
from database.db_executor import execute_sql
from llm.llm_explainer import explain_result
from rag.rag_utils import retrieve_context
from llm.openai_llm import llm


def chatbot(question: str) -> str:
    """
    Universal School Data Chatbot
    - Handles ANY natural language question
    - Chooses SQL or RAG dynamically using LLM
    """

    # -----------------------------
    # STEP 1: Decide question type
    # -----------------------------
    qtype = classify_question_llm(llm, question)

    # =============================
    # SQL / ANALYTICS PATH
    # =============================
    if qtype == "SQL":

        sql = generate_sql(llm, question)

        if sql == "NOT_POSSIBLE":
            return (
                "This question cannot be answered using the "
                "available dataset."
            )

        columns, rows = execute_sql(sql)

        if not rows:
            return "No matching records found for this question."

        return explain_result(llm, columns, rows, question)

    # =============================
    # RAG / DESCRIPTIVE PATH
    # =============================
    context = retrieve_context(question)

    if not context.strip():
        return (
            "I could not find relevant information in the dataset "
            "to answer this question."
        )

    rag_prompt = f"""
You are an educational data analyst.

Use ONLY the information provided in the context.
Do NOT use outside knowledge.

Rules:
- Analyze patterns across students
- Summarize trends at group level
- Do NOT describe individual students
- Do NOT copy raw records
- Do NOT invent data
- Answer in 4–6 clear bullet points

Context:
{context}

Question:
{question}
"""

    return llm(rag_prompt)