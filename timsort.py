TS_min= 32
  
TS_comp_count = 0
TS_swap_count = 0
TS_comp_count_mat = 0
TS_swap_count_mat = 0

def timsort(array):
    try:
        global TS_comp_count
        global TS_swap_count
        TS_comp_count = 0
        TS_swap_count = 0
        timsort_sort(array)
    finally:
        return [TS_comp_count, TS_swap_count]

    
    
def timsort_sort(array):
    global TS_comp_count
    global TS_swap_count

    n = len(array) 
    minrun = TS_find_minrun(n) 

    for start in range(0, n, minrun): 
        end = min(start + minrun - 1, n - 1) 
        TS_insertion_sort(array, start, end) 

    size = minrun 
    while size < n: 

        for left in range(0, n, 2 * size): 

            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            TS_merge(array, left, mid, right) 

        size = 2 * size 
    
        


def TS_find_minrun(n): 
    global TS_comp_count
    global TS_swap_count
    r = 0
    while n >= TS_min:
        TS_comp_count +=1
        r |= n & 1
        n >>= 1
    return n + r

def TS_insertion_sort(array, left, right): 
    global TS_comp_count
    global TS_swap_count
    for i in range(left+1,right+1):
        element = array[i]
        TS_swap_count+=1
        j = i-1
        while element<array[j] and j>=left :
            TS_comp_count += 2
            array[j+1] = array[j]
            TS_swap_count+=1
            j -= 1
        array[j+1] = element
        TS_swap_count+=1
    return array

def TS_merge(array, l, m, r): 
    global TS_comp_count
    global TS_swap_count
  
    array_length1= m - l + 1
    array_length2 = r - m 
    left = []
    right = []
    for i in range(0, array_length1): 
        left.append(array[l + i]) 
        TS_swap_count+=1
    for i in range(0, array_length2): 
        right.append(array[m + 1 + i]) 
        TS_swap_count+=1
  
    i=0
    j=0
    k=l
   
    while j < array_length2 and  i < array_length1: 
        TS_comp_count += 1
        TS_comp_count += 1
        if left[i] <= right[j]: 
            array[k] = left[i] 
            TS_swap_count+=1
            i += 1
  
        else: 

            array[k] = right[j] 
            TS_swap_count+=1
            j += 1
  
        k += 1
  
    while i < array_length1: 
        TS_comp_count += 1
        array[k] = left[i] 
        TS_swap_count+=1
        k += 1
        i += 1
  
    while j < array_length2: 
        TS_comp_count += 1
        array[k] = right[j] 
        TS_swap_count+=1
        k += 1
        j += 1

