import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # 👈 THIS IS CRITICAL

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful educational data analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=300
    )
    return response.choices[0].message.content.strip()