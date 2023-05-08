import os

import requests
from dotenv import load_dotenv


load_dotenv()

SERVICE_ENDPOINT = os.getenv('SERVICE_ENDPOINT')


def get_new_question_and_answer():
    response = requests.get(SERVICE_ENDPOINT)
    response_json = response.json()[0]
    question = response_json.get('question')
    answer = response_json.get('answer')
    return question, answer
