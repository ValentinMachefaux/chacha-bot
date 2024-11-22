import os
from mistralai import Mistral
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

mistral_api_key = os.getenv("MISTRAL_API_KEY")
if not mistral_api_key:
    raise ValueError("There's no API_KEY. Check if you've correctly defined your MISTRAL_API_KEY in the .env.")

# Mistral model config
model = "mistral-large-latest"
client = Mistral(api_key=mistral_api_key)

temp_ai = input("choose the number temp for ai, between 0 and 1 \n the more it is the more creative the ai is. \n >> ")
while True:
    question = input("Ask a question to Mistral (or 'exit' to quit): ")

    if question.lower() == "exit":
        print("Conversation ended.")
        break

    try:

        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": question,
                },
            ],
            temperature=temp_ai,  # Adjust the temperature if needed
        )

        print("Mistral's response:")
        responseM = chat_response.choices[0].message.content
        format_responseM = responseM.replace(". ", ".\n")
        print(format_responseM)

    except Exception as e:
        print(f"Error: {e}")
