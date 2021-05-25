class human:
    def __init__(self, age, name,family):
        self._age = age
        self.name = name
        self.family = family

class family:
    def __init__(self, mother,father):
        self.mother = mother
        self.father = father
        self.childrens = []

    def add_child(self, child):
        self.childrens.append(child)

class simple:
    def __init__(self):
        pass
    
    @classmethod
    def func(self,a,b):
        return a*b

class complex(simple):
    def __init__(self):
        pass
    
    @classmethod
    def method(self,a):
        return super().func(a,2) + a


        
