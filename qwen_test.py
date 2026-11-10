
import requests
import json

MODEL = "qwen2.5"

url = "http://localhost:11434/api/generate"

prompt = """
List exactly 5 Tamil month names in traditional order.

Rules:
1. Number them from 1 to 5.
2. Use English transliteration.
3. Do not add explanations.
4. Output exactly 5 names.
"""

payload = {
    "model": MODEL,
    "prompt": prompt,
    "stream": False,
    "options": {
        "temperature": 0.7
    }
}

try:
    response = requests.post(
        url,
        json=payload,
        timeout=300
    )

    response.raise_for_status()

    result = response.json()

    print("\n===== QWEN 2.5 RESPONSE =====\n")
    print(result["response"])

except requests.exceptions.ConnectionError:
    print("Error: Ollama is not running.")

except requests.exceptions.RequestException as error:
    print("API Error:", error)
