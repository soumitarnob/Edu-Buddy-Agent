from backend.agents.study_agent import study_agent
from backend.memory.memory import memory


class ChatService:

    def chat(self, question: str):

        answer = study_agent.run(question)

        memory.save(question, answer)

        return {
            "answer": answer
        }


chat_service = ChatService()