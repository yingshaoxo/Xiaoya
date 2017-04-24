import sys
import telebot
from __Xiaoya__ import xiaoya

TGx = xiaoya('xiaoya', 17, 'telegram', '__all__')
bot = telebot.TeleBot("121899714:AAF3xShKMc52iV5yN93fiIjOH98ZXP1zcOc")

@bot.message_handler(commands=['start'])
def send_welcome(msg):
    bot.reply_to(msg, "Hi~")

@bot.message_handler(commands=['go'])
def handle(msg):
    #print(msg)
    result = TGx.reply(msg.text)
    if result != '':
        bot.reply_to(msg, result)

@bot.message_handler(content_types=['text'])
def handle(msg):
    #print(msg)
    result = TGx.reply(msg.text)
    if result != '':
        bot.reply_to(msg, result)

bot.polling()
