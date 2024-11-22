import os
from dotenv import load_dotenv
from functions.drive import download_file
from functions.pdf_extractor import extract_text_from_pdf
from functions.mistral_interaction import ask_mistral

# Loading environment variables
load_dotenv()

mistral_api_key = os.getenv("MISTRAL_API_KEY")
if not mistral_api_key:
    raise ValueError("Thre's no MISTRAL_API_KEY. Check if you've defined it in the .env.")

drive_api_key = os.getenv("DRIVE_API_KEY")
if not drive_api_key:
    raise ValueError("Thre's no DRIVE_API_KEY. Check if you've defined it in the .env.")

file_id = "19UwHFZlriYPcQJlGBE5fSUO6E1UIaZKP"
temp_pdf_path = "./temp.pdf"


def main():
    try:
        download_file(file_id, drive_api_key, temp_pdf_path)
        pdf_content = extract_text_from_pdf(temp_pdf_path)

        while True:
            question = input("Ask about the document ('exit' to stop) : ")
            if question.lower() == "exit":
                print("End of session.")
                break

            response = ask_mistral(pdf_content, question, mistral_api_key)
            print(response)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)
            print("Temporary PDF file removed.")


if __name__ == "__main__":
    main()
