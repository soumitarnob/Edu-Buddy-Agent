import os

print("Starting EduBuddy...")

os.system("uvicorn backend.main:app --reload")