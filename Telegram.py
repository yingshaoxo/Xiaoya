import telebot
from __Xiaoya__ import xiaoya

TGx = xiaoya('xiaoya', 17, 'telegram', '__all__')
bot = telebot.TeleBot("121899714:AAF3xShKMc52iV5yN93fiIjOH98ZXP1zcOc")

@bot.message_handler(commands=['start'])
def send_welcome(msg):
    if msg.chat.type == 'supergroup':
        bot.reply_to(msg.chat.id, 'You send start to me.')

@bot.message_handler(commands=['stop'])
def send_welcome(msg):
    if msg.chat.type == 'supergroup':
        bot.reply_to(msg.chat.id, 'You send stop to me.')

@bot.message_handler(commands=['schedule'])
def handle(msg):
    if msg.chat.type == 'supergroup':
        bot.reply_to(msg.chat.id, 'You send schedule to me.')

@bot.message_handler(commands=['chat_id'])
def handle(msg):
    if msg.chat.type == 'supergroup':
        bot.reply_to(msg.chat.id, 'Chat_id of this group:\n{}'.format(str(msg.chat.id)))
        
@bot.message_handler(content_types=['text'])
def handle(msg):
    result = TGx.reply(msg.text)
    if result != '':
        bot.reply_to(msg, result)

bot.polling()
