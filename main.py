import os

from dotenv import load_dotenv
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

from service import get_new_question_and_answer

load_dotenv()
API_KEY = os.getenv('api_key')

bot = Bot(token=API_KEY)
updater = Updater(token=API_KEY)

Q_Answer = {}


def start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,
                             text='Hello, could you play the game? '
                                  'Send for the start \n/new_question')


def send_question(update, context):
    chat = update.effective_chat
    question, answer = get_new_question_and_answer()
    Q_Answer[chat.id] = [question, answer]
    context.bot.send_message(chat_id=chat.id,
                             text=f'Question: {question}\n\n'
                                  f'Answer: {answer}')


def check_answer(update, context):
    chat = update.effective_chat
    text = update.message.text
    try:
        if text.lower() == Q_Answer[chat.id][1].lower():
            context.bot.send_message(chat_id=chat.id,
                                     text='Correct!!! \n /new_question')
        else:
            context.bot.send_message(chat_id=chat.id,
                                     text='Sorry, is`s not correct, next try or \n'
                                          '/new_question')
    except KeyError:
        context.bot.send_message(chat_id=chat.id,
                                 text='Use /start to get started')


if __name__ == '__main__':
    updater.dispatcher.add_handler(CommandHandler('new_question', send_question))
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, check_answer))
    updater.start_polling()
