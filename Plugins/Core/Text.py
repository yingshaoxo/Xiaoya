import re

def text_to_sentences(text):
    def handle(obj):
        text = obj.group(0).strip('  　\n ')
        return text + '\n'*2
    text = re.sub(r'((.*?)(?<!B|A)([！？。]))', handle, text)
    a_list = text.split('\n')
    a_list = [i.strip('  　\n ') for i in a_list if re.match(r'^\s*$', i) == None]
    text = '\n'.join(a_list)
    return text.strip('  　\n ')

def text_to_list(text, split_string='\n\n' + '——————————————' + '\n\n'):
    result = text.split(split_string)
    if result == [text]:
        result = text.split('\n')
    result = [i.strip('  　\n ') for i in result if re.match(r'^\s*$', i) == None]
    return result

def list_to_text(list_, split_string='\n\n' + '——————————————' + '\n\n'):
    return split_string.join(list_)

def language_check(text):
    if re.match(r'[\u4e00-\u9fa5]', text) is None:
        return 'English'
    else:
        return 'Chinese'
