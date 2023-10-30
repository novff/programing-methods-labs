def qsort(arr): 
    QS_compare_counter = 0
    QS_swap_counter = 0
    l = 0
    h = len(arr) - 1
    size = h - l + 1
    stack = [0] * (size)
    top = -1
    
    top = top + 1
    stack[top] = l 
    QS_swap_counter+=1
    top = top + 1
    stack[top] = h 
    QS_swap_counter+=1
    
    while top >= 0: 
        QS_compare_counter += 1
        h = stack[top] 
        QS_swap_counter+=1
        top = top - 1
        l = stack[top] 
        QS_swap_counter+=1
        top = top - 1
    
        p = QS_partition( arr, l, h ) 
        
        if p-1 > l: 
            QS_compare_counter += 1
            top = top + 1
            stack[top] = l 
            QS_swap_counter+=1
            top = top + 1
            stack[top] = p - 1
            QS_swap_counter+=1
        
        if p + 1 < h: 
            QS_compare_counter += 1
            top = top + 1
            stack[top] = p + 1
            QS_swap_counter+=1
            top = top + 1
            stack[top] = h 
            QS_swap_counter+=1

    print("кол-во сравнений: "+ str(QS_compare_counter) +" \nкол-во подмен: " + str(QS_swap_counter))



def QS_partition(arr, l, h): 
    i = ( l - 1 ) 
    x = arr[h] 

    for j in range(l, h): 
        if arr[j] <= x:
            #
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] 
            

    arr[i + 1], arr[h] = arr[h], arr[i + 1] 
    return (i + 1) 