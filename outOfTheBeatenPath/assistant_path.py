import os
import openai
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

def get_api_key():
    """
    Func get apy_key from .env file
    :return: apy_key - str
    """
    load_dotenv(find_dotenv(), override=True)
    apy_key = os.getenv("OPENAI_API_KEY")
    return apy_key

def chat_clone():
    """
    Func modulate chat assistant to help user
    :return: interactive chat assistant
    """
    openai.api_key = get_api_key()

    client = OpenAI()

    messages = []
    system_role_content = 'Suggest travel destinations out of the beaten path instead of the mainstream destinations'
    messages.append({'role': 'system', 'content': system_role_content})
    print('Welcome to the Travel Chat powered by OpenAI!')
    print("Type your travel question, or type 'exit' to end.")
    while True:

        # user interaction
        user_input = input('You: ')
        if user_input.lower() in ['exit','quit','q']:
            print('Thank you for using Travel Chat powered by OpenAI!')
            break
        if user_input.lower() == '':
            continue

        # process information
        messages.append({'role':'user', 'content': user_input})

        response = client.chat.completions.create(
            model='gpt-4.1-mini',
            messages=messages,
            temperature=0.7,
            max_tokens=3000
        )
        assistant_answer = response.choices[0].message.content

        messages.append({'role':'assistant', 'content': assistant_answer})

        # return answer
        print('AI: ', assistant_answer)



# 'I need get suntan on free beach. I am in Amersfoort in Netherland. Beach have to be in 15 km aproximaty.
chat_clone()
