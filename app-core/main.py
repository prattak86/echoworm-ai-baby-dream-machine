# app-core/main.py

import os
from inference.llm_client import LLMClient
from agent import EchoWormAgent
from dotenv import load_dotenv

load_dotenv()

def main():
    print("🧠 EchoWorm Baby Dream Machine™")
    print("Type 'exit' to quit.\n")

    backend = os.getenv("LLM_BACKEND", "ollama")
    client = LLMClient(backend=backend)
    agent = EchoWormAgent(llm_client=client)

    while True:
        try:
            user_input = input("You: ")
            if user_input.strip().lower() == "exit":
                break

            response = agent.think(user_input)
            print(f"EchoWorm: {response}\n")

        except KeyboardInterrupt:
            print("\n[Interrupted]")
            break
        except Exception as e:
            print(f"[Error] {e}")

if __name__ == "__main__":
    main()
