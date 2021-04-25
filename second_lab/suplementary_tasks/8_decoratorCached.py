from functools import wraps

from functools import wraps
import time


class RecursiveDict(dict):
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            self[item] = self.__class__()
            value = self[item]
            return value

def cached(func):
    saved=RecursiveDict()

    @wraps(func)
    def newfunc(*args, **kwargs):
        st=' '.join('{0}{1}'.format(key, val) for key, val in sorted(kwargs.items()))
        if saved[args][st] == {}:
            result = func(*args, **kwargs)
            saved[args][st] = result
            return result
        else:
            print("Cached!")
            return saved[args][st]
    return newfunc

@cached
def simple(a,b):
    return a*b

#print(simple(5, 6))
print(simple(5,b=6))
print(simple(5,b=6))
print(simple(a=5,b=6))
print(simple)