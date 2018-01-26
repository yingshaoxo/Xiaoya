import telebot
from __Xiaoya__ import xiaoya

user_id = 'telegram'
directory = 'programming'
TGx = xiaoya('xiaoya', 17, user_id, directory)

GROUP = -1001027434973
TOKEN = '121899714:AAF3xShKMc52iV5yN93fiIjOH98ZXP1zcOc'


x = xiaoya('xiaoya', 17, 'telegram', '__all__')
bot = telebot.TeleBot("121899714:AAF3xShKMc52iV5yN93fiIjOH98ZXP1zcOc")

@bot.message_handler(commands=['chat_id'])
def get_chat_id(msg):
    if msg.chat.type == 'supergroup':
        reply = 'Chat_id of this group:\n\n{}'.format(str(msg.chat.id))
        reply += '\n\n' + '-'*20 + '\n\n' + 'Who sent this message:\n\n{}'.format(str(msg.from_user.id))
        bot.reply_to(msg, reply)
        
@bot.message_handler(commands=['go'])
def send_a_piece_of_knowledge(msg):
    if msg.chat.id != GROUP:
        return
    result = x.reply(msg.text)
    if result != '':
        bot.reply_to(msg, result)

@bot.message_handler(content_types=['text'])
def handle(msg):
    r = x.translate(msg.text)
    if r != '':
        bot.reply_to(msg, r)

bot.polling()
