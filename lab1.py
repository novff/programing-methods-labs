'''
comparing qsort and timsort 
'''
from functools import wraps
import time
import csv
#decorator timer
def recordTime(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

def writeArrays():
    arr1 = []
    arr2 = []
    for a in range(0,5001):
        if a % 2 == 0:
            arr1.append(a)
        else:
            arr2.append(a)
    with open("f1.txt", "w") as f:
        wr = csv.writer(f, delimiter=";", quotechar="'", quoting=csv.QUOTE_ALL)
        wr.writerow(arr1)
    with open("f2.txt", "w") as f:
        wr = csv.writer(f, delimiter=";", quotechar="'", quoting=csv.QUOTE_ALL)
        wr.writerow(arr2)


'''
    everything requiered for the tim sort algoritm
'''

#@recordTime
#def timsort():
'''
    everything requiered for the quick sort algoritm
'''
#@recordTime
#def qsort():


    



def main():
    writeArrays()


main()
    