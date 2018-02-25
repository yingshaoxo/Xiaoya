import telebot
from __Xiaoya__ import xiaoya

TOKEN = '121899714:AAF3xShKMc52iV5yN93fiIjOH98ZXP1zcOc'

x = xiaoya('xiaoya', 17, 'telegram', '__all__')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['chat_id'])
def get_chat_id(msg):
    if msg.chat.type == 'supergroup':
        reply = 'Chat_id of this group:\n\n{}'.format(str(msg.chat.id))
        reply += '\n\n' + '-'*20 + '\n\n' + 'Who sent this message:\n\n{}'.format(str(msg.from_user.id))
        bot.reply_to(msg, reply)
        
@bot.message_handler(commands=['go'])
def send_a_piece_of_knowledge(msg):
    result = x.reply(msg.text)
    if result != '':
        bot.reply_to(msg, result)

@bot.message_handler(content_types=['text'])
def handle(msg):
    if not x.is_English(msg.text) and msg.chat.title in ['Python for English']:
        admin_list = bot.get_chat_administrators(msg.chat.id)
        admin_ids = [member.user.id for member in admin_list]
        
        if msg.from_user.id in admin_ids:
            bot.reply_to(msg, 'Please speak English!')
        else:
            bot.kick_chat_member(msg.chat.id, msg.from_user.id)
            bot.unban_chat_member(msg.chat.id, msg.from_user.id)

bot.polling()
