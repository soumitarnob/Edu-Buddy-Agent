from langchain_google_genai import ChatGoogleGenerativeAI

from backend.config import settings


class LLMService:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=settings.MODEL_NAME,
            google_api_key=settings.GOOGLE_API_KEY,
            temperature=0.3
        )


llm_service = LLMService()