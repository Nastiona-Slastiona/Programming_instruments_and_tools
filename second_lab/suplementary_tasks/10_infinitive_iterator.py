class InfiniteIterator:
    def __init__(self, some_object):
        self.some_object=None
        self.index=0
        try:
            iterator = iter(some_object)
        except TypeError:
            print("object is not iterable")
        else:
            self.some_object = some_object

    def __next__(self):
        try:
            result = self.some_object[self.index]
        except IndexError:
            self.index=0
            result = self.some_object[self.index]
        self.index += 1
        return result

    def filter(self, func):
        filtered_object = self.some_object
        index = 0
        while True:
            try:
                result = filtered_object[index]
            except IndexError:
                return InfiniteIterator(filtered_object)
            if func(filtered_object[index]) == False:
                del filtered_object[index]
            else: index += 1

    def __iter__(self):
        return self

inf_b = InfiniteIterator(4)
a = [1, 2, 3, 4]
inf_a = InfiniteIterator(a)
print(inf_a.some_object)

def more_than_two(x):
    if x > 2:
        return True
    else:
        return False

filtered_inf_a=inf_a.filter(more_than_two)
print(filtered_inf_a.some_object)
