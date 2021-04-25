import inspect
import datetime

def log(method,name):
    def time(*args,**kwargs):
        result = method(*args,**kwargs)
        now = datetime.datetime.now()
        with open("{}.txt".format(name), "w") as my_file:
            my_file.write('time: {}\nВызван метод с именем: {} у класса с именем: {}\n'.format(now,method.__name__,name))
            my_file.write('Аргументы: {}\n'.format((args, kwargs)))
            my_file.write('Его резлультат: {}\n\n'.format(result))
            my_file.close()
        return result
    return time 

class Logger(object):

    def __getattribute__(self, s):
        attr = super(Logger, self).__getattribute__(s)
        if inspect.ismethod(attr): 
            return log(attr, self.__class__.__name__)
        else:
            return attr


    def __str__(self):
        with open("{}.txt".format(self.__class__.__name__),'r') as log_file:
            return log_file.read()

class Example(Logger):
    def simple_example(self,a,b):
        return a + b

y = Logger()
x = Example()
x.simple_example(4,5)
print(x)