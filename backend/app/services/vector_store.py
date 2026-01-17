import chromadb
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.collection = self.client.get_or_create_collection(
            name="arthasarathi_phase1"
        )

    def add_documents(self, texts, metadatas):
        embeddings = self.model.encode(texts).tolist()
        ids = [str(i) for i in range(len(texts))]

        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )

    def retrieve(self, query, k=3):
        query_embedding = self.model.encode([query]).tolist()

        return self.collection.query(
            query_embeddings=query_embedding,
            n_results=k
        )
