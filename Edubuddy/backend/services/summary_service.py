from backend.services.llm_service import llm_service


class SummaryService:

    def summarize(self, context: str):

        prompt = f"""
Summarize the following text.

Text:

{context}
"""

        return llm_service.llm.invoke(prompt).content


summary_service = SummaryService()