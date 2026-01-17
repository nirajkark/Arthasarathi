from fastapi import APIRouter
from backend.app.services.vector_store import VectorStore
from backend.app.services.llm import generate_answer
from backend.app.services.evaluation import evaluate

router = APIRouter()
store = VectorStore()

@router.post("/ask")
def ask(question: str):
    results = store.retrieve(question)

    context = " ".join(results["documents"][0])

    answer = generate_answer(question, context)
    metrics = evaluate(answer, context)

    return {
        "question": question,
        "answer": answer,
        "evaluation": metrics
    }
