from langchain_core.tools import tool
from backend.services.summary_service import summary_service


@tool
def summary_tool(text: str):

    """
    Summarize study material.
    """

    return summary_service.summarize(text)