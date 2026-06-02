import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("pragma table_info(students);")
columns = cursor.fetchall()

print("📊 Columns in table:")
for col in columns:
    print(col)

conn.close()
