from gigachat import GigaChat
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())
CREDENTIALS = os.getenv("CREDENTIALS")


def get_answer(query):
  with GigaChat(credentials=CREDENTIALS, verify_ssl_certs=False, model='GigaChat-Plus') as giga:
    response = giga.chat(query)
    return response.choices[0].message.content