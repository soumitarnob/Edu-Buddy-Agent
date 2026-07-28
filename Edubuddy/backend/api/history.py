from fastapi import APIRouter

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def upload_home():

    return {
        "message": "History API is working"
    }