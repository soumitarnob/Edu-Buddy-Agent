from backend.services.llm_service import llm_service


class FlashcardService:

    def generate(self, context: str):

        prompt = f"""
Create 10 flashcards.

Format:

Q:
A:

Text:

{context}
"""

        return llm_service.llm.invoke(prompt).content


flashcard_service = FlashcardService()