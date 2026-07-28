from backend.services.llm_service import llm_service


class QuizService:

    def generate(self, context: str):

        prompt = f"""
Generate 10 MCQs.

Each should have

A

B

C

D

Correct Answer

Text:

{context}
"""

        return llm_service.llm.invoke(prompt).content


quiz_service = QuizService()