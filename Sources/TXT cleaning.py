import re

virsion = str(8)
if virsion == '0':
    virsion = ''
book = '英语说话力：美国人天天在说的口语大全集.txt'
book2 = book.replace('.txt', virsion+'.txt')
with open(book2, 'r', encoding='utf-8') as f:
    text = f.read()

#您上月在此我们
line = '\n\n' + '——————————————' + '\n\n'
#do something in here
##def handle(obj):
##    text = obj.group(0)
##    return text + '\n'
##text = re.sub(r'B：.*', handle, text)

all_list = text.split(line)
##all_list_result = []
##for piece in all_list:
##    all_sentense = [i.strip('  　\n ') for i in piece.split('\n') if re.match(r'^\s*$', i) == None]
##    all_sentense_result = ''
##    for num, i in enumerate(all_sentense, start=1):
##        if num == 1:
##            all_sentense_result += i + '\n\n\n'
##        else:
##            all_sentense_result += i + '\n'
##    all_list_result.append(all_sentense_result)
##    
text = line.join([i.strip('  　\n ') for i in all_list])

#text = text.replace('', '')
#text = text[:-len(line)]
#text = text.strip('  　\n ')
#print(text)
#do something in here


if virsion == '':
    virsion = '0'
book2 = book.replace('.txt', str(int(virsion)+1)+'.txt')
with open(book2, 'w', encoding='utf-8') as f:
    f.write(text)
