import sqlite3
from config import Config

class Memory:
    def __init__(self):
        self.conn = sqlite3.connect(Config.DB_PATH, check_same_thread=False)
        self._init_schema()

    def _init_schema(self):
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt TEXT,
                response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            );
            """)

    def store_interaction(self, prompt, response):
        with self.conn:
            self.conn.execute("INSERT INTO memory (prompt, response) VALUES (?, ?)", (prompt, response))

    def fetch_context(self, limit=5):
        cur = self.conn.cursor()
        cur.execute("SELECT prompt, response FROM memory ORDER BY id DESC LIMIT ?", (limit,))
        return cur.fetchall()
