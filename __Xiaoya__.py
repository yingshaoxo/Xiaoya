#from Plugins.HandleText import text_tool
import random
import json
import os
import re

class _os():
    '''reading and writing for json'''
    def __init__(self):
        self.dir = os.path.join(os.path.dirname(__file__), 'Sources') #A directory path saving thoese txt files.
        if not os.path.exists(self.dir):
            os.mkdir(self.dir)
        self.setting_file_path = os.path.join(self.dir, 'setting.json') #A json file to save schedule

    def get_setting(self):
        with open(self.setting_file_path, 'r') as f:
            text = f.read()
        return json.loads(text)

    def write_setting(self, a_dict):
        with open(self.setting_file_path, 'w') as f:
            f.write(json.dumps(a_dict, sort_keys=True, indent=4))

    def split_txt_to_list(self, file_name):
        try:
            with open(file_name, 'r',  encoding='utf-8', errors='ignore') as f: 
                text = f.read()
        except Exception as e:
            print(e)
            print('We only support UTF_8!')
        result = text.split('\n\n' + '——————————————' + '\n\n')
        if result == [text]:
            result = text.split('\n')
        result = [i for i in result if re.match(r'^\s*$', i) == None]
        return result


class walker(_os):
    '''look for files in dir'''
    def __init__(self, directory):
        super().__init__()
        self.directory = directory

    def get_txt_list(self):
        if self.directory == '__all__':
            all_files = []
            for root, dirs, files in os.walk(self.dir):
                for name in files:
                    all_files.append(os.path.join(root, name))
            txt_files = [name for name in all_files if '.txt' == name[-4:]]
        elif self.directory == '__main__':
            main_files = [os.path.join(self.dir, name) for name in os.listdir(self.dir) if '.txt' == name[-4:]]
            return main_files
        else:
            main_files = [os.path.join(self.dir, name) for name in os.listdir(self.dir) if '.txt' == name[-4:]]
            directory_files = [os.path.join(self.dir, self.directory, name) for name in os.listdir(os.path.join(self.dir, self.directory)) if '.txt' == name[-4:]]
            txt_files = main_files + directory_files
        return txt_files

    def get_txt_name(self):
        return [os.path.basename(name) for name in self.get_txt_list()]

    def get_dir_list(self):
        return [name for name in os.listdir(self.dir) if os.path.isdir(os.path.join(self.dir, name))]


class update(walker):
    '''update setting file'''
    def __init__(self, user_id, directory):
        super().__init__(directory)
        self.user_id = str(user_id)
        self.initialize_setting() #auto initializtion

    def initialize_setting(self):
        if not os.path.exists(self.setting_file_path): #create a new setting json file
            self.write_setting({
                self.user_id:{
                    self.directory: {}
                    }
                })
            
        self.setting = self.get_setting() #update user_id
        if self.user_id not in list(self.setting.keys()): ##make sure user_id in setting##
            self.setting.update({
                self.user_id: {}
                })
        
        self.user_setting = self.setting.get(self.user_id) #update directory
        if self.directory not in list(self.user_setting.keys()): ##make sure directory in user_id##
            self.user_setting.update({
                self.directory: {}
                })
        directory_list = self.get_dir_list()
        for directory in directory_list: ##add new dir to json
            if directory not in self.user_setting.keys():
                self.user_setting.update({
                    directory: {}
                    })
        for json_directory in list(self.user_setting.keys()): ##del non-exists dir in json
            if json_directory not in directory_list and json_directory != '__all__' and json_directory != '__main__':
                del self.user_setting[json_directory]

        self.user_txt_setting = self.user_setting.get(self.directory) #update txt
        txt_list = self.get_txt_name()
        if self.user_txt_setting == {}:
            for txt in txt_list:
                self.user_txt_setting.update({txt:0})
        else:
            for name in txt_list: ##add new txt to json
                if name not in self.user_txt_setting.keys():
                    self.user_txt_setting.update({name:0})
            for json_name in list(self.user_txt_setting.keys()): ##del non-exists txt in json
                if json_name not in txt_list:
                    del self.user_txt_setting[json_name]

        self.write_setting(self.setting) #save change

    def update_schecule(self, txt_name):
        '''just reading num + 1'''
        old_num = self.user_txt_setting.get(txt_name)
        new_num = old_num + 1
        self.user_txt_setting.update({txt_name: new_num})
        self.write_setting(self.setting)
        return old_num

    def how_many_left(self):
        '''find out how many pieces left for reading'''
        txt_files = self.get_txt_list()
        
        all_list_length = 0 #find out how many pieces in all
        for txt in txt_files:
            one_list_length = len(self.split_txt_to_list(txt))
            all_list_length += one_list_length

        all_progress_length = 0 #find out how many pieces already read
        progress_list = self.user_txt_setting.values()
        for i in progress_list:
            all_progress_length += i

        return all_list_length - all_progress_length


class knowledge(update):
    def __init__(self, user_id, directory='__main__'):
        super().__init__(user_id, directory)

    def get_random_one(self):
        all_txt = self.get_txt_list()
        book_path = random.choice(all_txt)
        book_pieces = self.split_txt_to_list(book_path)
        book_name = os.path.basename(book_path)
        num = self.update_schecule(book_name)
        try:
            one = book_pieces[num]
        except:
            one = 'You finished your reading with ' + book_name + '.'
            try:
                os.rename(book_path, book_path.replace('.txt', '.bak'))
            except:
                os.remove(book_path)
        return one

    def get_left_num(self):
        return self.how_many_left()


class skill():
    def __init__(self, user_id, directory):
    	self.user_id = user_id
    	self.directory = directory

    def knowledge(self, func='one_piece'):
        k = knowledge(self.user_id, self.directory)
        if func == 'one_piece':
            text = k.get_random_one()
            text = text.replace('\n', '\n'*2)
            '''text_list = text.split('\n')
            text_list.reverse()
            text = '\n'.join(text_list)'''
            return text
        elif func == 'left_num':
            return k.get_left_num()

    def baike(self, key_word):
        from Plugins.Extensions.GetBaike.Baike import main as baike
        from Plugins.Extensions.GetChinese.SplitSentence import main as split_Ch
        return split_Ch(baike(key_word))
    
    def translate(self, text):
        from Plugins.Extensions.GetEnglish.SplitSentenceAndTranslate import main as translate
        return translate(text)

    def run_python(self, codes):
        from __RunPY__ import run_py_codes
        return run_py_codes(codes)    


class xiaoya(skill):
    '''A real xiaoya class'''
    def __init__(self, name, age, user_id, directory):
        self.name = name
        self.age = age
        super().__init__(user_id, directory)
        #print(self.about())

    def about(self):
        return ("My name is {name}.\nAnd I'm {age} years old now.\n".format(name=self.name, age=self.age))

    def reply(self, msg):
        from Plugins.Core.Text import language_check
        #print('replying...')
        msg = msg.strip('  　\n ')
        if msg[:6] == '#codes':
            msg = msg.replace('#codes', '').strip('  　\n ')
            if msg != '':
                return self.run_python(msg)
        if language_check(msg) == 'Chinese':
            if len(msg) <= 10:
                return self.baike(msg)
        return self.knowledge('one_piece')

    def left_num(self):
        return self.knowledge('left_num')


##x = xiaoya('xiaoya', 17, 'telegram', '__all__')
##print(x.left_num())
##print(x.reply('#codes\nimport os\nprint(os.system("ls"))'))
##print(x.reply('#baike good'))
