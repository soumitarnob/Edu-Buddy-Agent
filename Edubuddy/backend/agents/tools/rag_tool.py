from langchain.tools import tool

from backend.rag.chain import ask


@tool
def rag_tool(question: str):

    """
    Answer questions using uploaded documents.
    """

    return ask(question)