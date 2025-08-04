from config import Config

class ModelInterface:
    def __init__(self):
        if Config.MODEL_BACKEND == "openai":
            from models import openai_model
            self.model = openai_model.OpenAIModel()
        elif Config.MODEL_BACKEND == "llama":
            from models import llama_model
            self.model = llama_model.LLaMaModel()
        else:
            raise NotImplementedError("Unsupported model backend")

    def generate_response(self, prompt, context=None):
        return self.model.generate(prompt, context)
