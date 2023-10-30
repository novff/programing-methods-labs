TS_min= 32
  


def timsort(array):
    
    n = len(array) 
    minrun = TS_find_minrun(n) 
  
    for start in range(0, n, minrun): 
        swapcounter()
        end = min(start + minrun - 1, n - 1) 
        TS_insertion_sort(array, start, end) 
   
    size = minrun 
    while size < n: 
        comparecounter()
        for left in range(0, n, 2 * size): 
  
            mid = min(n - 1, left + size - 1) 
            swapcounter()
            right = min((left + 2 * size - 1), (n - 1)) 
            swapcounter()
            TS_merge(array, left, mid, right) 
  
        size = 2 * size 
    print("кол-во сравнений: "+ str(TS_counter_compare) +" \nкол-во подмен: " + str(TS_counter_swap))

def TS_find_minrun(n): 
    r = 0
    while n >= TS_min:
        comparecounter()
        r |= n & 1
        n >>= 1
    return n + r

def TS_insertion_sort(array, left, right): 
    for i in range(left+1,right+1):
        element = array[i]
        swapcounter()
        j = i-1
        while element<array[j] and j>=left :
            comparecounter()
            array[j+1] = array[j]
            swapcounter()
            j -= 1
        array[j+1] = element
    return array

def TS_merge(array, l, m, r): 
  
    array_length1= m - l + 1
    array_length2 = r - m 
    left = []
    right = []
    for i in range(0, array_length1): 
        left.append(array[l + i]) 
        swapcounter()
    for i in range(0, array_length2): 
        right.append(array[m + 1 + i]) 
        swapcounter()
  
    i=0
    j=0
    k=l
   
    while j < array_length2 and  i < array_length1: 
        comparecounter()
        if left[i] <= right[j]: 
            comparecounter()
            array[k] = left[i] 
            swapcounter()
            i += 1
  
        else: 
            comparecounter()
            array[k] = right[j] 
            swapcounter()
            j += 1
  
        k += 1
  
    while i < array_length1: 
        comparecounter()
        array[k] = left[i] 
        swapcounter()
        k += 1
        i += 1
  
    while j < array_length2: 
        comparecounter()
        array[k] = right[j] 
        swapcounter()
        k += 1
        j += 1
TS_counter_compare = 0
TS_counter_swap = 0
def swapcounter():
    global TS_counter_swap
    TS_counter_swap +=1
def comparecounter():
    global TS_counter_compare
    TS_counter_compare +=1

