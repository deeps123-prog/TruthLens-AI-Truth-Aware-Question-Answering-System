from models.llm import call_llm

def generate_answer(query, context):
    prompt = f"""
Answer using ONLY the context.

Question: {query}
Context: {context}

Return JSON:
{{
  "answer": "...",
  "key_points": ["..."]
}}
"""
    return call_llm(prompt)
