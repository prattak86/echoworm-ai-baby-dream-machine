# app-core/agent.py

class EchoWormAgent:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.memory = []

    def think(self, user_input):
        self.memory.append(user_input)

        prompt = f"The user said: {user_input}\nRespond with a curious, reflective tone:"
        response = self.llm.generate(prompt)

        self.memory.append(response)
        return response
