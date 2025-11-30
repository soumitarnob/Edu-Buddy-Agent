# EduBuddy – AI Learning Companion
Kaggle 5-Day AI Agents Intensive – Capstone Project

## Problem Statement
Students often struggle with long study materials and time-consuming revision. Creating summaries, flashcards, and quizzes manually takes a lot of effort. EduBuddy solves this problem by automatically summarizing content, generating flashcards, creating quizzes, and storing learning sessions to support efficient personalized studying.

## Why Agents?
Agents can break down complex tasks into multiple steps, call tools autonomously when needed, and maintain memory across sessions. This makes the entire study workflow—searching, summarizing, flashcard creation, quiz generation—fast, adaptive, and intelligent.

## What I Created (Overall Architecture)
EduBuddy is built with a modular agent architecture:

1. Agent Core  
   - Handles user requests  
   - Chooses which tool to use  
   - Logs actions  
   - Manages workflow  

2. Tools  
   - Web Search Tool (simulated)  
   - Summarizer (LLM-stub)  
   - Flashcard Generator  
   - Quiz Generator  
   - Code Execution Tool  

3. Memory System  
   - JSON-based memory  
   - Stores previous sessions and long-term notes  

4. Workflow  
   User Input → Web Search → Summarization → Flashcards → Quiz → Save to Memory

## Demo – How to Run
Run the project using:
python edubuddy_agent.py

The agent will automatically:
- Perform a simulated search  
- Generate a summary  
- Create flashcards  
- Generate quiz questions  
- Store everything in memory  
- Print clean structured output

## The Build – Tools & Technologies Used
- Python 3  
- Custom agent logic  
- JSON memory storage  
- Logging for traceability  
- Fully offline (no external APIs)

Project Structure:
- edubuddy_agent.py  
- memory_bank.json  
- README.md  
- .gitignore  
- requirements.txt

## If I Had More Time
- Add real LLM integration (GPT, LLaMA, Gemini)  
- Add real web search APIs  
- Improve long-term memory with insights  
- Create a Streamlit/Gradio UI  
- Add support for PDFs, videos, webpages  
- Build an automated study planner agent  
