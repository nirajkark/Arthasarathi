from fastapi import FastAPI

app = FastAPI(
    title="Arthasarathi – Phase 1 MVP",
    description="Evaluation-aware RAG system",
    version="0.1.0"
)

@app.get("/")
def health():
    return {"status": "ok", "phase": 1}
