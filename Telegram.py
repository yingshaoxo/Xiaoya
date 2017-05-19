import datetime
import time

import telebot
from __Xiaoya__ import xiaoya

import multiprocessing


user_id = 'telegram'
directory = 'GaoKao'
TGx = xiaoya('xiaoya', 17, user_id, directory)

GROUP = -1001082405980
#GROUP = -178341019
TOKEN = '121899714:AAF3xShKMc52iV5yN93fiIjOH98ZXP1zcOc'
tb = telebot.AsyncTeleBot(TOKEN)

start_time = datetime.datetime(2017, 5, 20, 17)
work_days = 5 # all the day you got

work_time = datetime.timedelta(hours=work_days*24) 
end_time = start_time + work_time #deadline

all_interval = work_time.total_seconds()



def job_interval_time():
    diff = end_time - datetime.datetime.now()
    now_interval = diff.total_seconds()

    left_num = TGx.left_num()
    left_day = int(now_interval / (60 * 60 * 24)) - 1
    
    today_left_seconds = ((end_time - datetime.timedelta(hours=left_day*24)) - datetime.datetime.now()).total_seconds()

    interval_t = ((left_day * (8 * 60 * 60))+today_left_seconds) // left_num
    
    #progress = str((1 - (now_interval/all_interval)) * 100)[:7] + '%'
    if interval_t < 0:
        tb.send_message(GROUP, 'Your schedule times up!')
        exit()
        
    return left_num, interval_t

def job():
    result = TGx.reply('fuck')
    if result != '':
        tb.send_message(GROUP, result)
    return ''

def do():
    while True:
        left_num, interval_t = job_interval_time()
        #tb.send_message(-1001120909649, 'You still got {} pieces to read.'.format(left_num))
        #tb.send_message(-1001120909649, 'Every {} seconds one piece.'.format(str(int(interval_t))))
        job()
        time.sleep(interval_t)

task = multiprocessing.Process(target=do)

x = xiaoya('xiaoya', 17, 'telegram', '__all__')
bot = telebot.TeleBot("121899714:AAF3xShKMc52iV5yN93fiIjOH98ZXP1zcOc")

@bot.message_handler(commands=['chat_id'])
def handle(msg):
    if msg.chat.type == 'supergroup':
        bot.reply_to(msg, 'Chat_id of this group:\n\n{}'.format(str(msg.chat.id)))

@bot.message_handler(commands=['start_task'])
def handle(msg):
    if msg.chat.type == 'supergroup':
        if task.is_alive() == False:
            task.start()

@bot.message_handler(commands=['stop_task'])
def handle(msg):
    if msg.chat.type == 'supergroup':
        if task.is_alive() == True:
            task.terminate()
        
@bot.message_handler(content_types=['text'])
def handle(msg):
    result = x.reply(msg.text)
    if result != '':
        bot.reply_to(msg, result)

task.start()
bot.polling()
