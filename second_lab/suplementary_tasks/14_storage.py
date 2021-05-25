import re
import json

class my_set:  
    def __init__(self, some_set):  
        if isinstance(some_set, set):
            self.busted_set = some_set
        elif isinstance(some_set, list) or isinstance(some_set, list): 
            self.busted_set = set(some_set)
        else: raise TypeError  
  
    def busted_set_list(self):
        print(self.busted_set)
  
    def add(self, some_set):
        if isinstance(some_set, set) or isinstance (some_set, list):
            self.busted_set.update(some_set)
        else: raise TypeError

    def find(self, some_set):
        if isinstance(some_set, list) or isinstance (some_set, list):
            for i in some_set:
                if i in self.busted_set:
                    print(i)
                else: return False
            return True
        else: raise TypeError

    def remove(self, some_object):
        try:
            self.busted_set.remove(some_object)
        except KeyError:
            pass
    
    def grep(self, pattern):
        p=re.compile(pattern)
        find_list=p.findall(str(self.busted_set))
        print(find_list)
        return find_list

    def save(self, path):
        with open(path, "w") as write_file:
            self.busted_set = list(self.busted_set)
            json.dump(self.busted_set, write_file)
    def load(self,path):
        with open(path, "r") as read_file:
            self.busted_set = set(json.load(read_file))

# a={1,2,3,4}
# b=my_set(a)
# b.busetd_set_list()
# b.add([1,2,3,4,4,5,6,7,8,8,8,8])
# b.remove(2)
# print(b.find([1,3]))
# b.busetd_set_list()
# b.grep('\d+')

custom_set = my_set([])
while True:
    comand = input()
    if(comand.startswith('quit')):
        break
    elif(comand.startswith('save')):
        text = comand.split(" ")
        custom_set.save(text[1])
    elif(comand.startswith('load')):
        text = comand.split(" ")
        custom_set.load(text[1])
    elif(comand.startswith('grep')):
        text = comand.split(" ")
        custom_set.grep(text[1])
    elif(comand.startswith('list')):
        custom_set.busted_set_list()
    elif(comand.startswith('remove')):
        text = comand.split(" ")
        if(text[1] == 'int'):
            custom_set.remove(int(text[2]))
        elif(text[1] == 'float'):
            custom_set.remove(float(text[2]))
        elif(text[1] == 'bool'):
            custom_set.remove(bool(text[2]))
        else:
            custom_set.remove(text[1])            
    elif(comand.startswith('add')):
        text = comand.split("  ")
        stroka = text[2]
        stroka = stroka.replace('[',"")
        stroka = stroka.replace(']',"")
        stroka = stroka.replace(',',"")
        text1 = stroka.split(" ")
        our_list = []
        if(text[1] == 'int'):
            for i in text1:
                our_list.append(int(i))
        elif(text[1] == 'float'):
            for i in text1:
                our_list.append(float(i))
        elif(text[1] == 'bool'):
            for i in text1:
                our_list.append(bool(i))
        elif(text[1] == 'str'):
            for i in text1:
                our_list.append(i)
        custom_set.add(our_list)

    elif(comand.startswith('find')):
        text = comand.split("  ")
        stroka = text[2]
        stroka = stroka.replace('[',"")
        stroka = stroka.replace(']',"")
        stroka = stroka.replace(',',"")
        text1 =  stroka.split(" ")
        our_list=[]
        if(text[1] == 'int'):
            for i in text1:
                our_list.append(int(i))
        elif(text[1] == 'float'):
            for i in text1:
                our_list.append(float(i))
        elif(text[1] == 'bool'):
            for i in text1:
                our_list.append(bool(i))
        elif(text[1] == 'str'):
            for i in text1:
                our_list.append(i)
            custom_set.find(our_list)   
        
