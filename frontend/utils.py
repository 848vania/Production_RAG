import requests 

API_BASE_URL = "http://localhost:8000"

def ask_question(question: str) -> dict:
    response = requests.post(
        f"{API_BASE_URL}/chat/",
        json = {
            "question": question
        },
        timeout = 60,
    )
    response.raise_for_status()
    print(response.json())
    return response.json()