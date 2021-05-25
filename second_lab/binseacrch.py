def binsearch(value, array):
    if len(array) > 1:
        i = round((len(array)/2))
        if value < array[i]:
            return binsearch(value,array[0:i])
        elif value > array[i]:
            return binsearch(value,array[i:])
        else:
            print("FIND!")
            return True
    else:
        return False
        
    
def main():
    mylist = (2,3,5,6,8,9)
    print(binsearch(5, mylist))

if __name__ == '__main__':
    main()
