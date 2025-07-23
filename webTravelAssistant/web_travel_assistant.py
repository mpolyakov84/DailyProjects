import gradio as gr
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


def get_travel_advice(message):
    """
    return the travel advice
    :param message: input question from user
    :return: str answer
    """

    client = genai.Client(api_key=get_api_key())

    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=message,
        config=GenerateContentConfig(
            system_instruction=[
                "You are a travel assistant.",
                "You give advice for out of the beaten path places."
            ]
        )
    )

    return response.text

# User request tips -  Give me ideas for a beach holiday around Amersfoort'


iface = gr.Interface(fn=get_travel_advice, inputs="text", outputs="markdown", title="✈️ Hidden Gems Travel Assistant",
                     description="Get advice on lesser-known travel destinations.")
iface.launch(share=True)
