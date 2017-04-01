import sys
import time
import telepot
from __Xiaoya__ import xiaoya

x = xiaoya('xiaoya', 17, 'telegram')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        text = str(msg['text'].replace('@XiaoyaBot', '').strip('  　\n '))
        #print(text)
        result = x.reply(text)
        if result != '':
            bot.sendMessage(chat_id, x.reply(text))

TOKEN = '121899714:AAF3xShKMc52iV5yN93fiIjOH98ZXP1zcOc'

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print('Listening...')

#Keep running.
while 1:
	time.sleep(10)
