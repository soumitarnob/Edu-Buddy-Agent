from dotenv import load_dotenv
import os

load_dotenv()

class Settings:

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    MODEL_NAME = os.getenv("MODEL_NAME")

    CHROMA_PATH = os.getenv("CHROMA_PATH")

    UPLOAD_PATH = os.getenv("UPLOAD_PATH")

    DATABASE_URL = os.getenv("DATABASE_URL")


settings = Settings()