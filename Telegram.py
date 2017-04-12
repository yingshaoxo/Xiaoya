import sys
import telebot
from __Xiaoya__ import xiaoya

x = xiaoya('xiaoya', 17, 'telegram')
bot = telebot.TeleBot("121899714:AAF3xShKMc52iV5yN93fiIjOH98ZXP1zcOc")

@bot.message_handler(commands=['start', 'hi'])
def send_welcome(msg):
    bot.reply_to(msg, "Hi~")

@bot.message_handler(content_types=['text'])
def handle(msg):
    result = x.reply(msg.text)
    if result != '':
        bot.reply_to(msg, result)

bot.polling()
