def custom_range(start, stop=None, step=1):
    if (stop == None):
        stop = start
        start = 0
    if step == 0:
        return []
    if (((step > 0) & (start >= stop)) | ((step < 0) & (start <= stop))) :
        return []
    result = []
    i = start
    if(step > 0):
       while i < stop:
            result.append(i)
            i += step 
    else:
        while i > stop :
            result.append(i)
            i += step
    return result

for i in custom_range(10, 1, -2):
    print(i)