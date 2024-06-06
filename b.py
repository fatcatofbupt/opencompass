import requests
import json
def ask_llm(query):
    url = "http://localhost:8000/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer EMPTY"
    }
    data = {
        "model": "qwen",
        "messages": [{"role": "user", "content": query}],
        "temperature": 0
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    info = response.json()
    res = info.get("choices")[0]['message'].get("content")
    return res