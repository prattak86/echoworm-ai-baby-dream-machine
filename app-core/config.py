import os

class Config:
    MODEL_BACKEND = os.getenv("MODEL_BACKEND", "openai")  # or "llama", "mistral"
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DB_PATH = os.getenv("DB_PATH", "memory.db")
