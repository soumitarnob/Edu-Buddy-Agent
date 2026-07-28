from langchain_core.tools import tool
from backend.services.flashcard_service import flashcard_service



@tool
def flashcard_tool(text: str):

    """
    Create flashcards.
    """

    return flashcard_service.generate(text)