import os
from mistralai import Mistral
from dotenv import load_dotenv
import requests
import pdfplumber

load_dotenv()

mistral_api_key = os.getenv("MISTRAL_API_KEY")

if not mistral_api_key:
    raise ValueError("Thre's no API_KEY. Check if you've correctly defined your MISTRAL_API_KEY in the .env.")

drive_api_key = os.getenv("DRIVE_API_KEY")
if not drive_api_key:
    raise ValueError("Thre's no API_KEY. Check if you've correctly defined your DRIVE_API_KEY in the .env.")

file_link = "https://drive.google.com/file/d/1sWuME3CJAfuGHnnYClbi8D1YpFnowp_W/view?usp=sharing"

def download_file(link, api_key, destination_path):
    url = f"{link}?alt=media&key={api_key}"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(destination_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # Évite les écritures vides
                    f.write(chunk)
        print(f"Fichier téléchargé avec succès : {destination_path}")
    else:
        print(f"Échec du téléchargement : {response.status_code} - {response.text}")

download_file(file_link, drive_api_key, "./temp.pdf")



model = "mistral-large-latest"
client = Mistral(api_key=mistral_api_key)

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

os.remove("./temp.pdf")
print("File successfully removed")