from models.llm import call_llm

def verify_answer(query, answer, context):
    prompt = f"""
Check the answer based on context.

Question: {query}
Answer: {answer}
Context: {context}

Return JSON:
{{
  "is_correct": true/false,
  "issues": ["..."],
  "revised_answer": "..."
}}
"""
    return call_llm(prompt)
