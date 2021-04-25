
class Defaultdict(dict):
    def __init__(self,default_factory):
        self.default_factory = default_factory
  
    def __getitem__(self,item):
        try: 
            return dict.__getitem__(self,item)
        except KeyError:
            return self.__missing__(item) 


    def __missing__(self, k):
        if self.default_factory == None:
            raise KeyError
        elif callable(self.default_factory):
            self[k] = self.default_factory()
        else:
            self[k] = self.default_factory
        value = self[k]
        return value
        
 
    def __str__(self):
        keys = list(self.keys())
        valuse = list(self.values())
        stroka = ''
        for i in range(len(keys)):
            stroka += '{}'.format(keys[i]) + ': ' + '{}'.format(valuse[i]) + ', '
        return '{'+ stroka + '}'
    
  
x = Defaultdict(dict)
x[2][4] = 23
x['m']['y'] = 4
x[34]
print(x)
