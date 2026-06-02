import sqlite3

def execute_sql(query: str):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    if not query.lower().startswith("select"):
        raise ValueError("Only SELECT queries allowed")

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    conn.close()
    return columns, rows