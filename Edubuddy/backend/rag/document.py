from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:

    def load_pdf(self, file_path: str):

        loader = PyPDFLoader(file_path)

        documents = loader.load()

        return documents


document_loader = DocumentLoader()