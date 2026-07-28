from fastapi import APIRouter

router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)


@router.get("/")
def upload_home():

    return {
        "message": "Quiz API is working"
    }