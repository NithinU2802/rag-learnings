import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ollama(question:str, context:str, config):
    # prompt = f"Context:\n{context}\n\nQuestion:\n{question}\n\nAnswer:"
    prompt = f"""
        You are an assistant that helps answer questions based on the provided context. Use the following context to answer the question:
        context: {context}
        question: {question}
        Please make sure to answer the question based on the context provided. If the answer is not present in the context, say "Please provide relevant question from the document".
    """
    response = requests.post(
        OLLAMA_URL,
        json={"model": config["ollama"]["llm_model"], "prompt": prompt, "stream": False},
    )

    data = response.json()

    if "response" not in data:
        raise ValueError(f"Response not found in Ollama response: {data}")
    return data["response"]
