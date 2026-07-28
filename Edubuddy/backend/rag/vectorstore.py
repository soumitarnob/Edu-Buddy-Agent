from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

from backend.config import settings


class VectorStore:

    def __init__(self):

        self.embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def save(self, documents):

        db = Chroma.from_documents(
            documents=documents,
            embedding=self.embedding,
            persist_directory=settings.CHROMA_PATH
        )

        db.persist()

        return len(documents)


vector_store = VectorStore()