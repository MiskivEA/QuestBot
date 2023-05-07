import os

from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from service import get_new_question_and_answer

load_dotenv()
API_KEY = os.getenv('api_key')
SERVICE_URL_API = 'http://jservice.io/'

bot = Bot(token=API_KEY)
updater = Updater(token=API_KEY)
chat_id = 303016224
info = 'Bot is activated. Use /start'

bot.send_message(chat_id=chat_id, text=f'{info}')


def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text='Hello, could you play the game? '
                                  'Send for the start /new_question')


def send_question(update, context):
    chat = update.effective_chat
    question, answer = get_new_question_and_answer()
    context.bot.send_message(chat_id=chat.id,
                             text=f'Question: {question}\n\n'
                                  f'Answer: {answer}')


updater.dispatcher.add_handler(CommandHandler('new_question', send_question))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
