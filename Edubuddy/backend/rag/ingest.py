from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.rag.document import document_loader
from backend.rag.vectorstore import vector_store


class IngestPipeline:

    def split_pdf(self, file_path: str):

        docs = document_loader.load_pdf(file_path)

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = splitter.split_documents(docs)

        return chunks

    def ingest(self, file_path: str):

        chunks = self.split_pdf(file_path)

        total = vector_store.save(chunks)

        return total


ingest_pipeline = IngestPipeline()