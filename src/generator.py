import os
from openai import OpenAI
from src.prompts import SYSTEM_PROMPT, build_user_prompt

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(question: str, retrieved_docs):
    if not retrieved_docs:
        return {
            "answer": "I don't have enough context to answer that.",
            "sources": [],
        }

    context = "\n\n".join(
        [f"Source: {doc['source']}\n{doc['text']}" for doc in retrieved_docs]
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(question, context)},
        ],
        temperature=0.2,
    )

    return {
        "answer": response.choices[0].message.content,
        "sources": [doc["source"] for doc in retrieved_docs],
    }