import os
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
if not api_key:
    raise ValueError("Thre's no API_KEY. Check if you've correctly defined your API_KEY in the .env.")

model = "mistral-large-latest"
client = Mistral(api_key=api_key)

try:
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Hello! Can you tell me about the weather?",
            },
        ],
    )
    print(chat_response.choices[0].message.content)
except Exception as e:
    print(f"Error happened : {e}")