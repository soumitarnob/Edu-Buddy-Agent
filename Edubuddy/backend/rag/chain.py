from langchain_core.output_parsers import StrOutputParser

from backend.rag.prompt import RAG_PROMPT
from backend.rag.retrieve import retriever
from backend.services.llm_service import llm_service


parser = StrOutputParser()


def ask(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    chain = (
        RAG_PROMPT
        | llm_service.llm
        | parser
    )

    answer = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return answer