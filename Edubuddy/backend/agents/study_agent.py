from backend.agents.router import detect_intent

from backend.agents.tools import (
    rag_tool,
    summary_tool,
    flashcard_tool,
    quiz_tool
)


class StudyAgent:

    def run(self, question):

        intent = detect_intent(question)

        if intent == "rag":

            return rag_tool.invoke({
                "question": question
            })

        if intent == "summary":

            return summary_tool.invoke({
                "text": question
            })

        if intent == "flashcard":

            return flashcard_tool.invoke({
                "text": question
            })

        if intent == "quiz":

            return quiz_tool.invoke({
                "text": question
            })

        return {
            "error": "Unable to determine the user's intent."
        }


study_agent = StudyAgent()