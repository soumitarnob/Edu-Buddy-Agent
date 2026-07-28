from fastapi import APIRouter

from backend.schemas.chat import ChatRequest

from backend.services.chat_service import chat_service


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/")

def chat(request: ChatRequest):

    return chat_service.chat(request.question)