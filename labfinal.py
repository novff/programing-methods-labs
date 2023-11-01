import csv
import copy
import timeit
import internal_arrays
import internal_matrix

from qsort import *
from timsort import *
from datetime import datetime

def readArray(fname):
    rdrArr = []
    with open(fname, "r") as file:
        rdr = csv.reader(file, delimiter=";")
        for a in rdr:
            rdrArr += a
    
    numArr = [int(x) for x in rdrArr]
    return numArr

def qsort_time(arr):
    a = copy.deepcopy(arr)
    t = timeit.Timer(lambda: qsort(a))
    print("Quicksort exec took: {}".format(t.timeit(1)))

def timsort_time(arr):
    a = copy.deepcopy(arr)
    t = timeit.Timer(lambda: timsort(a))
    print("Timsort exec took: {}".format(t.timeit(1)))

def timsort_matrix_time(arr):
    a = copy.deepcopy(arr)
    t = timeit.Timer(lambda: timsort_matrix(a))
    print("Timsort_matrix exec took: {}".format(t.timeit(1)))

def timsort_matrix(arr):
    for e in arr:
        timsort(e)
    timsort(arr)





def compare_sorts(arr):
    qsort_time(arr)
    timsort_time(arr)
    print("\n\n")
    

def external_sorting():
#в моей имплементации используется deepcopy, так что внутренняя и внешняя сортировка будут иметь одинаковый результат
    print("ВНЕШНЯЯ СОРТИРОВКА")

    print("сортировка продукта объединения массивов")
    merged_array = readArray("fmerge.txt")
    compare_sorts(merged_array)
    #readArray("f1.txt") + readArray("f2.txt")

    print("сортировка продукта перечисления массивов")
    intersection_array = readArray("fintersect.txt")
    #list(set(readArray("f1.txt")).intersection(set(readArray("f2.txt"))))
    compare_sorts(intersection_array)

    print("сортировка продукта разности массивов")
    difference_array = readArray("fdiff.txt")
    #list(set(readArray("f1.txt")).difference(set(readArray("f2.txt"))))
    compare_sorts(difference_array)

    print("сортировка продукта симмтеричной разности массивов")
    symmetric_diff_array = readArray("fsymmdiff.txt")
    #list(set(readArray("f1.txt")).symmetric_difference(set(readArray("f2.txt"))))
    compare_sorts(symmetric_diff_array)

 
def internal_sorting():
    print("ВНУТРЕННЯЯ СОРТИРОВКА")
    print("сортировка продукта объединения массивов")
    compare_sorts(internal_arrays.internal_merged)
    
    print("сортировка продукта перечисления массивов")
    compare_sorts(internal_arrays.internal_intersected)

    print("сортировка продукта разности массивов")
    compare_sorts(internal_arrays.internal_difference)

    print("сортировка продукта симмтеричной разности массивов")
    compare_sorts(internal_arrays.internal_symmetric_difference )



def main():
    #internal_sorting
    '''t1 = timeit.Timer(lambda: internal_sorting())
    print("INTERNAL SORTINGS TAKES: ",t1.timeit(1))
    
    print("\n")
    
    #external_sorting
    t2 = timeit.Timer(lambda: external_sorting())
    print("EXTERNAL SORTINGS TAKES: ", t2.timeit(1))
    '''
    
    print("сортировка матрицы 5000x5000")
    timsort_matrix_time(internal_matrix.internal_matrix)


main()

    