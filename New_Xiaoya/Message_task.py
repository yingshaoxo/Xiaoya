import datetime
import schedule
import time

import telebot
from __Xiaoya__ import xiaoya, update

user_id = 'books'
directory = 'GaoKao'
TGx = xiaoya('xiaoya', 17, user_id, directory)
Up = update(user_id, directory)

GROUP = -1001082405980
#GROUP = -178341019
TOKEN = '121899714:AAF3xShKMc52iV5yN93fiIjOH98ZXP1zcOc'
tb = telebot.TeleBot(TOKEN)


start_time = datetime.datetime(2017, 4, 22, 14)
work_days = 5 # all the day you got

work_time = datetime.timedelta(hours=work_days*24) 
end_time = start_time + work_time #deadline

all_interval = work_time.total_seconds()

def job_interval_time():
    diff = end_time - datetime.datetime.now()
    now_interval = diff.total_seconds()

    left_num = Up.how_many_left()
    left_day = int(now_interval / (60 * 60 * 24)) - 1
    
    if left_day == 0:
        left_day = 1

    interval_t = (left_day * (8 * 60 * 60)) // left_num
    #progress = str((1 - (now_interval/all_interval)) * 100)[:7] + '%'
    return left_num, interval_t

def job():
    result = TGx.reply('fuck')
    if result != '':
        tb.send_message(GROUP, result)
    return ''

left_num, interval_t = job_interval_time()
tb.send_message(GROUP, 'You still got {} pieces to read.'.format(left_num))
tb.send_message(GROUP, 'Every {} seconds one piece.'.format(str(int(interval_t))))
schedule.every(interval_t).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
