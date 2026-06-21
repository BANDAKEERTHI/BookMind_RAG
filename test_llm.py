from llm_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

response = llm.generate("What is artificial intelligence?")
print(response)
