import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет")
    print(message)

bot.polling(none_stop=True)