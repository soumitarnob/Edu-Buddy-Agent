from fastapi import APIRouter, UploadFile

from backend.services.upload_service import upload_service

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post("/")
def upload_pdf(file: UploadFile):

    return upload_service.upload(file)