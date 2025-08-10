import os

class Config:
    LLM_BACKEND = os.getenv("LLM_BACKEND", "ollama")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DB_PATH = os.getenv("DB_PATH", "memory.db")
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")