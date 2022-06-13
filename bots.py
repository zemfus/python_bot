import telebot
import datetime
bot = telebot.TeleBot("5126414010:AAFsQcjIpLCw5AovF2mZ2SwRVKTlevjFI-E")

@bot.message_handler(content_types=['text'])
def chatting(message):
    if message.text=='!ping':
        bot.reply_to(message, "Pong!")
bot.polling()
