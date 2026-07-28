from fastapi import APIRouter

router = APIRouter(
    prefix="/flashcard",
    tags=["Flashcard"]
)


@router.get("/")
def upload_home():

    return {
        "message": "Flashcard API is working"
    }