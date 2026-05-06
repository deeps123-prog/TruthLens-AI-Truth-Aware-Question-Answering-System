from openai import OpenAI
from app.config import OPENAI_API_KEY, MODEL_NAME, TEMPERATURE

client = OpenAI(api_key=OPENAI_API_KEY)

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
