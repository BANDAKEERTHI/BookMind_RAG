from agents.retrieval_agent import retrieve_context

import google.generativeai as genai
from langchain_community.llms import Ollama


def generate_answer(
    question,
    provider="Ollama",
    gemini_api_key="",
):
    context = retrieve_context(question)

    prompt = f"""
You are a helpful assistant.

Use ONLY the context below.

Context:
{context}

Question:
{question}

Answer in simple words.
"""

    print("\n===== CONTEXT =====")
    print(context[:1000])
    print("===================\n")

    # Gemini (BYOK)
    if provider == "Gemini":
        try:
            genai.configure(api_key=gemini_api_key)

            model = genai.GenerativeModel("gemini-2.0-flash")

            response = model.generate_content(prompt)

            return response.text

        except Exception:
            return (
                "Unable to generate response using Gemini. "
                "Please check your API key, quota, or billing settings."
            )

    # Ollama (Local AI)
    llm = Ollama(model="llama3.2:1b")

    response = llm.invoke(prompt)

    return response.strip() if isinstance(response, str) else response
