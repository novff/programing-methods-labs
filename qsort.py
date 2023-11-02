QS_comp_count = 0
QS_swap_count = 0

def qsort(arr): 
    global QS_comp_count
    global QS_swap_count
    QS_comp_count = 0
    QS_swap_count = 0
    qsort_sort(arr)
    return [QS_comp_count, QS_swap_count]


def qsort_sort(arr):
    global QS_comp_count
    global QS_swap_count

    l = 0
    h = len(arr) - 1
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    
    top = top + 1
    stack[top] = l 
    QS_swap_count+=1
    top = top + 1
    stack[top] = h 
    QS_swap_count+=1
    
    while top >= 0: 
        QS_comp_count += 1
        h = stack[top] 
        QS_swap_count +=1
        top = top - 1
        l = stack[top] 
        QS_swap_count +=1
        top = top - 1
    
        p = QS_partition( arr, l, h ) 

        QS_comp_count += 1
        if p-1 > l: 
            top = top + 1
            stack[top] = l 
            QS_swap_count+=1
            top = top + 1
            stack[top] = p - 1
            QS_swap_count+=1

        QS_comp_count += 1
        if p + 1 < h: 
            top = top + 1
            stack[top] = p + 1
            QS_swap_count+=1
            top = top + 1
            stack[top] = h 
            QS_swap_count+=1



def QS_partition(arr, l, h): 
    global QS_comp_count
    global QS_swap_count
    i = ( l - 1 ) 
    QS_swap_count+=1
    x = arr[h] 

    for j in range(l, h): 
        QS_comp_count+=1
        if arr[j] <= x:
            #
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] 
            QS_swap_count+=2
            

    arr[i + 1], arr[h] = arr[h], arr[i + 1] 
    QS_swap_count+=2
    return (i + 1) 