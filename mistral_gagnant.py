import os
from mistralai import Mistral
from dotenv import load_dotenv
import fitz
import requests

def download_file(file_id, api_key, destination_path):

    url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media&key={api_key}"
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(destination_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"File downloaded uccessfully : {destination_path}")
    else:
        print(f"Error when downloading : {response.status_code} - {response.text}")


def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        raise ValueError(f"Error when extracting the text : {e}")


# Loading var env
load_dotenv()

mistral_api_key = os.getenv("MISTRAL_API_KEY")
if not mistral_api_key:
    raise ValueError("Thre's no API_KEY. Check if you've correctly defined your MISTRAL_API_KEY in the .env.")

drive_api_key = os.getenv("DRIVE_API_KEY")
if not drive_api_key:
    raise ValueError("Thre's no API_KEY. Check if you've correctly defined your DRIVE_API_KEY in the .env.")

file_id = "19UwHFZlriYPcQJlGBE5fSUO6E1UIaZKP"

temp_pdf_path = "./temp.pdf"

try:

    download_file(file_id, drive_api_key, temp_pdf_path)

    pdf_content = extract_text_from_pdf(temp_pdf_path)
    # print(f"PDF extrait : {pdf_content[:500]}...")  # Just checking the pdf

    # Config for mistral
    model = "mistral-large-latest"
    client = Mistral(api_key=mistral_api_key)
    temp_ia = input("Choose the temp for the ai, between 0 and 1.\n The more the temp is , the more creative the ai is.")
    while True:
        question = input("Ask about the document ('exit' to stop) : ")
        if question.lower() == "exit":
            print("End of session.")
            break

        try:
            chat_response = client.chat.complete(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": f"Here's the document : {pdf_content}. Answer the questions by only using the given document.",
                    },
                    {
                        "role": "user",
                        "content": question,
                    },
                ],
                temperature=temp_ia,
            )
            print("Réponse de Mistral :")
            responseM = chat_response.choices[0].message.content
            format_responseM = responseM.replace(". ", ".\n")
            print(format_responseM)

        except Exception as e:
            print(f"Erreur lors de la requête Mistral : {e}")


except Exception as e:
    print(f"Erreur : {e}")

finally:

    if os.path.exists(temp_pdf_path):
        os.remove(temp_pdf_path)
        print("Fichier pdf temporaire supprimé.")
