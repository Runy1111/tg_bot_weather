import requests
import telebot
from tokens import bot_token
from weather import temperature

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, "Напиши /weather чтобы узнать погоду.")

    @bot.message_handler(commands=['weather'])
    def get_weather(message):
        bot.send_message(message.chat.id, f'Температура в москве сейчас: {temperature}')

    bot.polling()


if __name__ == '__main__':
    telegram_bot(bot_token)
