import requests


class OllamaLLM:
    def __init__(self, model="llama3"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        payload = {"model": self.model, "prompt": prompt, "stream": False}

        response = requests.post(self.url, json=payload)

        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Error: {response.text}"
