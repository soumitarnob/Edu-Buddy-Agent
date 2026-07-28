from fastapi import FastAPI

from backend.api import (
    chat,
    upload,
    summary,
    flashcard,
    quiz,
    history
)

app = FastAPI(
    title="EduBuddy API",
    version="1.0.0"
)

app.include_router(chat.router)
app.include_router(upload.router)
app.include_router(summary.router)
app.include_router(flashcard.router)
app.include_router(quiz.router)
app.include_router(history.router)


@app.get("/")
def home():

    return {
        "project": "EduBuddy",
        "status": "Running"
    }