def classify_question_llm(llm, question: str) -> str:
    prompt = f"""
You are a classifier.

Decide if the question requires:
- SQL (counts, filters, averages, comparisons, numbers)
- RAG (patterns, summaries, insights, explanations)

Reply ONLY with: SQL or RAG

Question:
{question}
"""
    return llm(prompt).strip().upper()