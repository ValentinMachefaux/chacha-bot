# Mistral PDF Query System
This Python project allows you to download a PDF file from Google Drive, extract its content, and interact with the Mistral AI model to ask questions based on the document's content. The model will answer your queries based only on the content of the provided PDF.

## Features

- **Download PDFs from Google Drive**: Uses the Google Drive API to fetch a file based on its ID.
- **PDF Text Extraction**: Extracts text from PDF files using the PyMuPDF (fitz) library.
- **Mistral AI Interaction**: Allows you to ask questions about the PDF content, with responses generated by the Mistral AI model.
- **Adjustable AI Creativity**: Set the "temperature" parameter of the AI to control its creativity, with a range from 0 (deterministic) to 1 (highly creative).
- **Interactive Session**: Keeps running until you type "exit", allowing multiple queries in a single session.

## Requirements

Before running the script, make sure you have the following Python libraries installed:

- `mistralai`: Python package to interact with the Mistral API.
- `requests`: To make HTTP requests to Google Drive API.
- `PyMuPDF`: Library to extract text from PDFs.
- `python-dotenv`: To load environment variables from a `.env` file.

You can install the required dependencies by running:
```bash
  pip install mistralai requests PyMuPDF python-dotenv
```
## Setup

1. **Get your API keys**:
   - [Mistral API Key](https://mistral.ai/)
   - [Google Drive API Key](https://console.cloud.google.com/apis/library/drive.googleapis.com)

2. Create a `.env` file in the root of the project to store your API keys:
    ```bash
      MISTRAL_API_KEY=your_mistral_api_key
      DRIVE_API_KEY=your_google_drive_api_key
    ```

3. Obtain the File ID:

   - For the file you want to use, copy the `file_id` from the URL. For example, from this link: https://drive.google.com/file/d/1sWuME3CJAfuGHnnYClbi8D1YpFnowp_W/view?usp=sharing, the file ID is `1sWuME3CJAfuGHnnYClbi8D1YpFnowp_W`.

## Usage

To use the script:

1. Run the Python script with the following command:
    ```bash
         python main.py
    ```

2. The script will prompt you for the temperature (AI creativity level). Enter a number between 0 and 1. The higher the number, the more creative the AI responses will be.

3. Then, you can start asking questions about the PDF content. Type your question and press Enter. The AI will respond based on the PDF's content.

4. Type `exit` to end the session.

> [!NOTE]
> If you want to use only the ai, just run the `renaud_ai.py`