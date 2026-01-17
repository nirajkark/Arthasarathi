from fastapi import FastAPI
from backend.app.api.ingest import router as ingest_router

from backend.app.api.ask import router as ask_router


app = FastAPI(
    title="Arthasarathi – Phase 1 MVP",
    description="Evaluation-aware RAG system",
    version="0.1.0"
)
app.include_router(ingest_router)
app.include_router(ask_router)
@app.get("/")
def health():
    return {"status": "ok", "phase": 1}
