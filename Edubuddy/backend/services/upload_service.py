import shutil
from pathlib import Path

from backend.config import settings
from backend.rag.ingest import ingest_pipeline


class UploadService:

    def upload(self, file):

        upload_dir = Path(settings.UPLOAD_PATH)

        upload_dir.mkdir(parents=True, exist_ok=True)

        file_path = upload_dir / file.filename

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(file.file, buffer)

        total_chunks = ingest_pipeline.ingest(str(file_path))

        return {

            "filename": file.filename,

            "chunks": total_chunks

        }


upload_service = UploadService()