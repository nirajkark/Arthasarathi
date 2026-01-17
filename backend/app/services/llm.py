import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_answer(question: str, context: str) -> str:
    prompt = f"""
You are a financial analyst.
Answer the question using ONLY the information in the context.
You may combine multiple sentences from the context.
Do NOT use external knowledge.
If the context indirectly supports an answer, explain the reasoning briefly.
If insufficient, say "Not enough information."

Context:
{context}

Question:
{question}
"""


    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
