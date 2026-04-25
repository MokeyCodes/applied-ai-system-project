SYSTEM_PROMPT = """
You are a careful study assistant.
Use only the provided context to answer.
If the context is insufficient, say that clearly.
Keep answers concise and accurate.
"""

def build_user_prompt(question: str, context: str) -> str:
    return f"""
Context:
{context}

Question:
{question}

Instructions:
- Answer only using the context above.
- If the answer is not supported by the context, say "I don't have enough context."
- Cite the source names you used.
"""