import datetime
import schedule
import time

import telebot
from __Xiaoya__ import xiaoya

TGx = xiaoya('xiaoya', 17, 'telegram')
TOKEN = '121899714:AAF3xShKMc52iV5yN93fiIjOH98ZXP1zcOc'
tb = telebot.TeleBot(TOKEN)

start_time = datetime.datetime(2017, 4, 21, 7)
work_time = datetime.timedelta(days=5) # all the day you got

all_interval = work_time.total_seconds()
end_time = start_time + work_time

diff = end_time - datetime.datetime.now()
now_interval = diff.total_seconds()

def job():
    diff = end_time - datetime.datetime.now()
    now_interval = diff.total_seconds()
    
    result = TGx.reply('fuck')
    if result != '':
        tb.send_message(131513300, result)

    progress = str((1 - (now_interval/all_interval)) * 100)[:7] + '%'
    print(progress)

left_num = TGx.task_num()
interval_t = now_interval // left_num
print(interval_t)
schedule.every(interval_t).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


