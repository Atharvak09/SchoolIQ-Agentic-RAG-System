def generate_sql(llm, question: str) -> str:
    prompt = f"""
You are an expert data analyst.

Database: school

Rules:
- Generate ONLY a SELECT query
- NEVER use DELETE, UPDATE, INSERT
- Use only columns that exist
- Do NOT hallucinate columns
- If question cannot be answered, reply: NOT_POSSIBLE

Schema:
school, sex, age, address, famsize, Pstatus,
Medu, Fedu, Mjob, Fjob, reason, guardian,
traveltime, studytime, failures,
schoolsup, famsup, paid, activities,
nursery, higher, internet, romantic,
famrel, freetime, goout,
Dalc, Walc, health, absences,
G1, G2, G3

Question:
{question}

SQL:
"""
    return llm(prompt).strip()