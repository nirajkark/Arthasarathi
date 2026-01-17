from fastapi import APIRouter
from backend.app.services.vector_store import VectorStore
from backend.app.services.news_ingest import get_sample_news

router = APIRouter()
store = VectorStore()

@router.post("/ingest")
def ingest():
    news = get_sample_news()

    store.add_documents(
        texts=news,
        metadatas=[{"source": "manual", "type": "news"} for _ in news]
    )

    return {"status": "ingested", "count": len(news)}
