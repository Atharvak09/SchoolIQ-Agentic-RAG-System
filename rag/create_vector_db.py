import sqlite3
import os
import pandas as pd

from langchain_community.document_loaders import DataFrameLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Connect to SQLite database
db_path = os.path.join("..", "database", "school.db")
conn = sqlite3.connect(db_path)

# Read SQL table
df = pd.read_sql_query("SELECT * FROM students", conn)
conn.close()

# Combine all columns into one text column
def row_to_text(row):
    return f"""
Student Record:
School: {row['school']}
Gender: {row['sex']}
Age: {row['age']}
Address: {row['address']}
Family Size: {row['famsize']}
Parent Status: {row['Pstatus']}
Mother Education: {row['Medu']}
Father Education: {row['Fedu']}
Study Time: {row['studytime']}
Failures: {row['failures']}
School Support: {row['schoolsup']}
Family Support: {row['famsup']}
Paid Classes: {row['paid']}
Activities: {row['activities']}
Internet Access: {row['internet']}
Free Time: {row['freetime']}
Go Out: {row['goout']}
Workday Alcohol: {row['Dalc']}
Weekend Alcohol: {row['Walc']}
Health: {row['health']}
Absences: {row['absences']}
Grade 1: {row['G1']}
Grade 2: {row['G2']}
Final Grade: {row['G3']}
"""

df["combined_text"] = df.apply(row_to_text, axis=1)


# Convert dataframe to documents
loader = DataFrameLoader(df, page_content_column="combined_text")
documents = loader.load()

# Load open-source embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create Chroma vector database
vector_db = Chroma.from_documents(
    documents,
    embedding_model,
    persist_directory="./chroma_db"
)

vector_db.persist()

print("✅ Vector database created successfully!")
