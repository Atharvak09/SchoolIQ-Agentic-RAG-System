def explain_result(llm, columns, rows, question):
    prompt = f"""
You are an educational data analyst.

Question:
{question}

Result Columns:
{columns}

Result Data:
{rows}

STRICT RULES:
- Use ONLY the values present in Result Data
- Do NOT assume causes
- Do NOT use outside knowledge
- Do NOT invent correlations
- If data does not show a relationship, say so
- Answer only based on visible numbers
- Respond in 4–6 bullet points
"""
    return llm(prompt)