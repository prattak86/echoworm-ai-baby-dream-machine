# app-core/main.py

import os
from inference.llm_client import LLMClient
from agent import EchoWormAgent
from dotenv import load_dotenv
from memory import Memory

load_dotenv()

def main():
    print("🧠 EchoWorm Baby Dream Machine™")
    print("Type 'exit' to quit.\n")
    memory = Memory() # Initialize memory for the agent
    backend = os.getenv("LLM_BACKEND", "ollama")
    client = LLMClient(backend=backend)

    # Read the default prompt
    prompt_path = os.path.join(os.path.dirname(__file__), "prompts", "default_prompt.txt")
    with open(prompt_path, "r") as f:
        default_prompt = f.read().strip()
    print("Loaded system prompt:\n", default_prompt)

    agent = EchoWormAgent(llm_client=client, memory=memory, default_prompt=default_prompt)

    while True:
        try:
            user_input = input("You: ")
            if user_input.strip().lower() == "exit":
                break

            response = agent.think(user_input)
            memory.store_interaction(user_input, response)
            print(f"EchoWorm: {response}\n")

        except KeyboardInterrupt:
            print("\n[Interrupted]")
            break
        except Exception as e:
            print(f"[Error] {e}")

if __name__ == "__main__":
    main()
