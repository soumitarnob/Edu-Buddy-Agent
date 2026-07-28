from langchain_core.tools import tool
from backend.services.quiz_service import quiz_service


@tool
def quiz_tool(text: str):

    """
    Generate quiz.
    """

    return quiz_service.generate(text)