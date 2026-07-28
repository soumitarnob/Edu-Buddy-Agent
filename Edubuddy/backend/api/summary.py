from fastapi import APIRouter

router = APIRouter(
    prefix="/summary",
    tags=["Summary"]
)


@router.get("/")
def upload_home():

    return {
        "message": "Summary API is working"
    }