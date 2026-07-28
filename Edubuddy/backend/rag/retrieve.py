from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from backend.config import settings


embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


db = Chroma(
    persist_directory=settings.CHROMA_PATH,
    embedding_function=embedding
)


retriever = db.as_retriever(
    search_kwargs={
        "k": 4
    }
)