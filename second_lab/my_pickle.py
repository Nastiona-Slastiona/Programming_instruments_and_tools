import pickle
import types
from pickler import RedefinitionPickle
from encoder import to_ser
from decoder import from_ser


class pickle_my():

    def __init__(self):
        pass

    def dump(self,obj,fp):
        with open(fp,'wb') as pickle_file:
            pickle.dump(to_ser(obj),pickle_file)
        

    def dumps(self,obj):
        try:
            return pickle.dumps(to_ser(obj))
        except Exception:
            return None

    def load(self,fp):
        with open(fp,'rb') as pickle_file:
            return from_ser(pickle.load(pickle_file))
        

    def loads(self,obj):
            return from_ser(pickle.loads(obj))
       
