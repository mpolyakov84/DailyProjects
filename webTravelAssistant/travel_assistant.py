from google import genai
from google.genai.types import GenerateContentConfig
from dotenv import load_dotenv, find_dotenv
import os


def get_api_key():
    """
    Find and return the api key
    :return: GOOGLE_API_KEY
    """
    load_dotenv(find_dotenv())
    return os.getenv("GOOGLE_API_KEY")


client = genai.Client(api_key=get_api_key())

chat = client.chats.create(
    model='gemini-2.0-flash',     #'gemini-1.5-flash-latest',
    config=GenerateContentConfig(
        system_instruction=[
            "You are a travel assistant.",
            "You give advice for out of the beaten path places."
        ]
    )
)

print('Hidden Gems Travel Assistant')
print('Get advice on lesser-known travel destinations from an AI travel assistant.')

while True:

    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'q']:
        print('Bye!')
        break

    res = chat.send_message(user_input)
    print('AI Travel Assistant: ', res.text)
