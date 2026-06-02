import pandas as pd
from sqlalchemy import create_engine

# Load CSV
csv_path = "../data/school.csv"
df = pd.read_csv(csv_path)

# Create SQLite database
engine = create_engine("sqlite:///school.db")

# Push CSV into SQL table
df.to_sql("students", engine, if_exists="replace", index=False)

print("✅ CSV successfully converted to SQL database!")
