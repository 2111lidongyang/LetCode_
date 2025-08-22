import requests
import json

url = "https://hyperai-tutorials-52iu46dtt95g.serv-c1.openbayes.net/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-cs200hvxgciksrbps2pgrepdrj4nc49e"
}

data = {
    "model": "EXAONE-4.0-32B",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "写一篇长篇文章描述LLM的发展历程"}
    ],
    "max_tokens": 8192
}

response = requests.post(url, headers=headers, json=data)
print(response.json())