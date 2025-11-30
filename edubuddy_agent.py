#!/usr/bin/env python3
import json
import os
import time
from typing import Dict, Any, List
import random
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')
logger = logging.getLogger('EduBuddy')

DATA_DIR = '/kaggle/working/edubuddy'
os.makedirs(DATA_DIR, exist_ok=True)
MEMORY_FILE = os.path.join(DATA_DIR, 'memory_bank.json')

class MemoryBank:
    def __init__(self, path=MEMORY_FILE):
        self.path = path
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        else:
            self.data = {'users': {}}
            self._save()

    def _save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def add_user(self, user_id: str):
        if user_id not in self.data['users']:
            self.data['users'][user_id] = {'sessions': [], 'long_term': {}}
            self._save()

    def add_session(self, user_id: str, session_state: Dict[str, Any]):
        self.add_user(user_id)
        self.data['users'][user_id]['sessions'].append(session_state)
        self._save()

    def set_long_term(self, user_id: str, key: str, value: Any):
        self.add_user(user_id)
        self.data['users'][user_id]['long_term'][key] = value
        self._save()

    def get_user(self, user_id: str):
        return self.data['users'].get(user_id, None)

memory = MemoryBank()

def llm_stub(prompt: str) -> str:
    responses = [
        "Sure — here's a concise summary of the material.",
        "I generated 10 flashcards focusing on core facts and concepts.",
        "Quiz ready: 5 MCQs with answers.",
        "I used web sources to supplement the answer and added citations.",
    ]
    return random.choice(responses) + " [LLM-stub response]."

def tool_web_search(query: str, top_k:int=3) -> List[Dict[str,str]]:
    logger.info(f"Tool:web_search called with query={query}")
    return [
        {'title': f'Simulated Article about {query} - {i+1}', 'snippet': 'Key point ...', 'url': f'https://example.com/{query}/{i+1}'}
        for i in range(top_k)
    ]

def tool_code_execute(code: str) -> Dict[str,Any]:
    logger.info('Tool:code_execute called')
    try:
        local = {}
        exec(code, {'__builtins__': {}}, local)
        return {'success': True, 'output': local}
    except Exception as e:
        return {'success': False, 'error': str(e)}

def tool_quiz_generator(topic: str, n_questions:int=5) -> List[Dict[str,Any]]:
    logger.info(f"Tool:quiz_generator called for topic={topic} n={n_questions}")
    qs = []
    for i in range(n_questions):
        qs.append({
            'question': f'What is a key point about {topic}? (sample question {i+1})',
            'options': ['A','B','C','D'],
            'answer': 'A'
        })
    return qs

class EduBuddyAgent:
    def __init__(self, user_id: str, memory: MemoryBank):
        self.user_id = user_id
        self.memory = memory
        memory.add_user(user_id)
        self.session = {'start_time': time.time(), 'actions': []}

    def log_action(self, action: Dict[str,Any]):
        self.session['actions'].append(action)
        logger.info('Agent action: ' + json.dumps(action, default=str))

    def summarize_material(self, input_text: str) -> str:
        prompt = f"Summarize the following text for a student:\n{input_text}\nMake it concise."
        res = llm_stub(prompt)
        self.log_action({'type':'summarize','prompt':prompt,'result_preview':res})
        return res

    def create_flashcards(self, summary: str, n:int=10) -> List[Dict[str,str]]:
        prompt = f"Generate {n} flashcards from this summary:\n{summary}"
        res = llm_stub(prompt)
        self.log_action({'type':'flashcards','prompt':prompt,'result_preview':res})
        cards = [{'front': f'What is {i+1}?', 'back': 'Short answer'} for i in range(n)]
        return cards

    def generate_quiz(self, topic: str, n:int=5):
        results = tool_quiz_generator(topic, n)
        self.log_action({'type':'quiz','topic':topic,'n':n})
        return results

    def use_web_search(self, query: str):
        hits = tool_web_search(query)
        self.log_action({'type':'web_search','query':query,'hits':hits})
        return hits

    def commit_session(self):
        self.session['end_time'] = time.time()
        self.memory.add_session(self.user_id, self.session)
        logger.info('Session committed to memory')

def demo_flow():
    agent = EduBuddyAgent(user_id='shaumi_01', memory=memory)
    user_request = "Study help: Probability Distributions. Give a 5-min summary, 8 flashcards, and 5 quiz questions."
    logger.info('User request: ' + user_request)
    hits = agent.use_web_search('Probability distributions overview for students')
    simulated_article_text = 'Probability distributions describe the likelihood of outcomes... (sample)'
    summary = agent.summarize_material(simulated_article_text)
    flashcards = agent.create_flashcards(summary, n=8)
    quiz = agent.generate_quiz('Probability distributions', n=5)
    agent.log_action({'type':'final_output','summary':summary,'num_flashcards':len(flashcards),'quiz_len':len(quiz)})
    agent.commit_session()
    return {'summary': summary, 'flashcards': flashcards, 'quiz': quiz}

if __name__ == '__main__':
    out = demo_flow()
    print('Demo output:')
    print(json.dumps(out, indent=2, ensure_ascii=False))
