import chromadb
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.collection = self.client.get_or_create_collection(
            name="arthasarathi_phase1",
            embedding_function=self._embed
        )

    def _embed(self, texts):
        return self.model.encode(texts).tolist()

    def add_documents(self, texts, metadatas):
        ids = [str(i) for i in range(len(texts))]
        self.collection.add(
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )

    def retrieve(self, query, k=3):
        return self.collection.query(
            query_texts=[query],
            n_results=k
        )
