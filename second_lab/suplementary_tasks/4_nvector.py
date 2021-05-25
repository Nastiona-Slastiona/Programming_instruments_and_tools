
class MY_Vect:
    def __init__(self,elements):
       self.elements = elements

    def add(self, another_vect):
        summ = []
        if len(another_vect) == len(self.elements):
            for i in range(len(self.elements)):
                 summ.append(self.elements[i] + another_vect.elements[i])
            return MY_Vect(summ)
        else:
            raise TypeError
        return None
    
    def sub(self,another_vect):
        diff = []
        if len(another_vect) == len(self.elements):
            for i in range(len(self.elements)):
                 diff.append(self.elements[i] - another_vect.elements[i])
            return MY_Vect(diff)
        else:
            raise TypeError
        return None

    def vector_len(self):
        square_sum = 0
        for element in self.elements:
            square_sum += element**2
        return square_sum**0.5
    
    def mul(self, chislo):
        for element in self.elements:
            element = element*chislo
    
    def vector_mul(self,another_vect):
        mul_result = 0
        if len(self.elements) == len(another_vect.elements):
            for i in range(len(self.elements)):
                mul_result += self.elements[i]*another_vect.elements[i]
            return mul_result
        else:
            raise TypeError
        return None
    
    def index(self, i):
        return self.elements[i]

    def to_string(self):
        for e in self.elements:
            return (','.join(str(e)))

    def equal(self,another_vect):
        return self.to_string() == another_vect.to_string()
    
vect1 = MY_Vect((1,2,3))
vect2 = MY_Vect((1,2,3))

print(vect1.vector_len())
print(vect1.equal(vect2))