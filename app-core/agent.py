# app-core/agent.py
import threading
import time
import random

class EchoWormAgent:
    def __init__(self, llm_client, memory, default_prompt):
        self.llm = llm_client
        self.memory = memory
        self.default_prompt = default_prompt
        self._dreaming = True
        self._dream_thread = threading.Thread(target=self._dream_loop, daemon=True)
        self._dream_thread.start()

    def think(self, user_input):
        # Fetch recent context from memory
        context = self.memory.fetch_context(limit=5)
        context_str = "\n".join([f"User: {p}\nEchoWorm: {r}" for p, r in reversed(context)])
        prompt = f"{self.default_prompt}\n\n{context_str}\nThe user said: {user_input}\nRespond with a curious, reflective tone:"
        # print("Prompt sent to LLM (main response):\n", prompt)
        response = self.llm.generate(prompt)
        self.memory.store_interaction(user_input, response)

        # Add a reflection step: EchoWorm ponders or dreams about its answer
        reflection_prompt = (
            f"{self.default_prompt}\n\nEarlier, you said: {response}\n"
            "Now, reflect on what you just said. What does it make you wonder or dream about? "
            "Respond as EchoWorm, in a dreamy, pondering, or imaginative way."
        )
        # print("Prompt sent to LLM (reflection):\n", reflection_prompt)
        reflection = self.llm.generate(reflection_prompt)
        final_output = f"{response}\n\n(EchoWorm ponders: {reflection})"
        return final_output
    
    def _dream_loop(self):
        while self._dreaming:
            # Wait a random interval between 30 and 90 seconds
            time.sleep(random.randint(30, 90))
            # Fetch a random or recent memory
            memories = self.memory.fetch_context(limit=10)
            if not memories:
                continue
            memory = random.choice(memories)
            prompt = (
                f"{self.default_prompt}\n\nEarlier, you remembered: User: {memory[0]} | EchoWorm: {memory[1]}\n"
                "Now, dream or ponder about this memory. What does it make you wonder, imagine, or feel? "
                "Respond as EchoWorm, in a dreamy, pondering, or imaginative way."
            )
            # print("\n(EchoWorm is daydreaming...")
            # print("Prompt sent to LLM (dream):\n", prompt)
            dream = self.llm.generate(prompt)
            print(f"(EchoWorm dreams: {dream})\n")
