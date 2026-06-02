import pandas as pd

df = pd.read_csv("data/school.csv")  # your file name

def handle_data_question(question: str):
    q = question.lower()

    try:
        # COUNT
        if "how many" in q or "count" in q:
            if "girl" in q:
                return f"There are {len(df[df['sex'] == 'F'])} girls."

            if "boy" in q:
                return f"There are {len(df[df['sex'] == 'M'])} boys."

            return f"There are {len(df)} students."

        # AVERAGE
        if "average" in q or "mean" in q:
            if "g3" in q or "final" in q:
                return f"Average final grade is {round(df['G3'].mean(),2)}"

            if "age" in q:
                return f"Average age is {round(df['age'].mean(),2)}"

        # MAX
        if "maximum" in q or "highest" in q:
            if "g3" in q:
                return f"Highest final grade is {df['G3'].max()}"

            if "age" in q:
                return f"Highest age is {df['age'].max()}"

        # MIN
        if "minimum" in q or "lowest" in q:
            if "g3" in q:
                return f"Lowest final grade is {df['G3'].min()}"

        return None

    except Exception as e:
        return f"Error: {str(e)}"