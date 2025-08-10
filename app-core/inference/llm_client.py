import os
import requests

class LLMClient:
    def __init__(self, backend="ollama"):
        self.backend = backend
        # Use OLLAMA_BASE_URL from environment, default to Docker Compose service name for containers
        self.base_url = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
        self.model = os.getenv("LLM_MODEL", "llama3")

    def generate(self, prompt):
        if self.backend == "ollama":
            return self._generate_ollama(prompt)
        raise ValueError(f"Unsupported backend: {self.backend}")

    def _generate_ollama(self, prompt):
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={"model": self.model, "prompt": prompt, "stream": False},
                timeout=30
            )
            response.raise_for_status()
            data = response.json()
            return data.get("response", "[No response]")
        except requests.RequestException as e:
            return f"[Ollama error: {e}]"
