import os
import json


class FileAttrMetaclass(type):

    def __new__(self, future_class, future_class_p, future_attr,**kargs):
        self.path = os.path.abspath(kargs.get('argpath'))
        cls_new_attr = {}
        with open(self.path,'r') as rfile:
            cls_new_attr = json.load(rfile)
        
        future_attr.update(cls_new_attr) 
        return type(future_class,future_class_p,future_attr)


class Lol(metaclass=FileAttrMetaclass, argpath='attr.json'):
    def print_cls(self):
        self.added_attr = []
        self.added_attr.append(','.join(each for each in self.__dir__() if not each.startswith("__")))
        for each in self.added_attr:
            print(each)
       

x = Lol()
x.print_cls()