def merge(left_list, right_list):  
    sorted_list = []
    left_list_index = right_list_index = 0
    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(nums):  
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums
    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2
    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)
#merge по времени О(nlogn), по памяти О(n) 

# Проверяем, что оно работает
random_list_of_nums = [120, 45, 68, 250, 176]  
random_list_of_nums = merge_sort(random_list_of_nums)  
print(random_list_of_nums)   

def partition(nums, low, high):  
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):  
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

random_list_of_nums = [22, 5, 1, 18, 99]  
quick_sort(random_list_of_nums)  
print(random_list_of_nums)    
#quick по времени О(nlogn) в среднем O(n^2) в худшем, по памяти О(1) 


# Counting sort’s computation order is O(n+k). Radix sort needs to run counting sort k times. 
# In total time complexity of radix sort is O(k(n+k)).
# Сложность по памяти O(n*k)
# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
def countingSort(arr, exp1): 
    n = len(arr) 
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
    # initialize count array as 0 
    count = [0] * (10) 
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i] / exp1) 
        count[int((index) % 10)] += 1
    # Change count[i] so that count[i] now contains actual 
    # position of this digit in output array 
    for i in range(1,10):
        count[i] += count[i-1] 
    # Build the output array 
    i = n - 1
    while i >= 0: 
        index = (arr[i]/exp1) 
        output[count[int((index) % 10)] - 1] = arr[i] 
        count[int((index) % 10)] -= 1
        i -= 1
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  
# Method to do Radix Sort
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr, exp)
        exp *= 10

# Driver code to test above
arr = [170, 45, 75, 90, 802, 24, 2, 66, 100]
radixSort(arr)
print(arr)
