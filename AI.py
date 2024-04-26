import google.generativeai as genai
import os

api_key = os.getenv('GOOGLE_API_KEY')

genai.configure()


safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

model = genai.GenerativeModel('gemini-pro',safety_settings=safety_settings)

def reading(card_data, question):
    print("reading your fortune")
    print(str(question))
    prompt = "Given this python dictionary of tarot cards, please give me a reading about " + str(question) + ":" + str(card_data) + " Please refrain from using asterisks. Thank you!"
    print(prompt)
    response = model.generate_content(prompt)
    print("response: " + str(response))
    return(response.text)
