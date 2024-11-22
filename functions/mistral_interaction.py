from mistralai import Mistral


def ask_mistral(pdf_content, question, mistral_api_key):
    model = "mistral-large-latest"
    client = Mistral(api_key=mistral_api_key)

    try:
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": f"Here's the document: {pdf_content}. Answer the questions by only using the given document.",
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
            temperature=0.5,  # Customize the temperature as per your needs
        )
        response = chat_response.choices[0].message.content
        # Format the response to improve readability (adding newlines after sentences)
        formatted_response = response.replace(". ", ".\n")
        return formatted_response
    except Exception as e:
        raise ValueError(f"Error with Mistral API: {e}")
