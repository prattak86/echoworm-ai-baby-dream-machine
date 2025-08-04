# # app-core/inference/llm_client.py
# import requests
# import os
# import openai

# class LLMClient:
#     def __init__(self, backend="ollama"):
#         self.backend = backend.lower()
#         self.model = os.getenv("LLM_MODEL", "llama3")
#         self.ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
#         self.openai_model = os.getenv("OPENAI_MODEL", "gpt-4")
#         self.openai_api_key = os.getenv("OPENAI_API_KEY", None)
#         openai.api_key = self.openai_api_key

#     def generate(self, prompt):
#         if self.backend == "ollama":
#             return self._query_ollama(prompt)
#         elif self.backend == "openai":
#             return self._query_openai(prompt)
#         else:
#             raise ValueError("Unsupported backend")

#     def _query_ollama(self, prompt):
#         response = requests.post(self.ollama_url, json={
#             "model": self.model,
#             "prompt": prompt,
#             "stream": False
#         })
#         response.raise_for_status()
#         return response.json().get("response")

#     def _query_openai(self, prompt):
#         response = openai.ChatCompletion.create(
#             model=self.openai_model,
#             messages=[{"role": "user", "content": prompt}]
#         )
#         return response['choices'][0]['message']['content']

# app-core/inference/llm_client.py

import os
import requests

class LLMClient:
    def __init__(self, backend="ollama"):
        self.backend = backend
        self.base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11436")

    def generate(self, prompt):
        if self.backend == "ollama":
            return self._generate_ollama(prompt)
        raise ValueError(f"Unsupported backend: {self.backend}")

    def _generate_ollama(self, prompt):
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False}
        )
        data = response.json()
        return data.get("response", "[No response]")
