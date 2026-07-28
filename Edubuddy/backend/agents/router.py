def detect_intent(question: str):

    q = question.lower()

    if "summary" in q:

        return "summary"

    if "flashcard" in q:

        return "flashcard"

    if "quiz" in q:

        return "quiz"

    return "rag"