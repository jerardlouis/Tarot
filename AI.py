import google.generativeai as genai
import os

api_key = os.getenv('GOOGLE_API_KEY')

genai.configure()

model = genai.GenerativeModel('gemini-pro')
def test():
    response = model.generate_content("What is the meaning of life?")

    return(response.text)
    

def reading(card_data):
    print("reading your fortune")
    print(card_data)
    prompt = "Given this python dictionary of tarot cards, please give me a reading about my future: " + str(card_data) + " Please refrain from using asterisks. Thank you!"
    print(prompt)
    response = model.generate_content(prompt)

    return(response.text)
