import csv
import copy
import timeit
import internal_arrays
import random

from qsort import *
from timsort import *
from datetime import datetime

sumcomp = 0
sumswap = 0

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
    t = timeit.Timer(lambda: get_returns(qsort(a)))
    print("Quicksort exec took: {}".format(t.timeit(1)))

def timsort_time(arr):
    a = copy.deepcopy(arr)
    t = timeit.Timer(lambda:get_returns(timsort(a)))
    print("Timsort exec took: {}".format(t.timeit(1)))

def timsort_matrix_time(arr):    
    a = copy.deepcopy(arr)
    t = timeit.Timer(lambda: timsort_matrix(a))

    print("Timsort exec took: {}".format(t.timeit(1)))

def qsort_matrix_time(arr):
    a = copy.deepcopy(arr)
    t = timeit.Timer(lambda: qsort_matrix(a))

    print("Qsort exec took: {}".format(t.timeit(1)))

def qsort_matrix(arr):
    sumcomp = 0
    sumswap = 0
    for e in arr:
        ret_e = qsort(e)
        sumcomp += ret_e[0]
        sumswap += ret_e[1]
    ret_arr = qsort(arr)
    sumcomp += ret_arr[0]
    sumswap += ret_arr[1]
    print("comparisons: " + str(sumcomp) + " swaps: " + str(sumswap))

def timsort_matrix(arr):
    sumcomp = 0
    sumswap = 0
    for e in arr:
        ret_e = timsort(e)
        sumcomp += int(ret_e[0])
        sumswap += int(ret_e[1])
    ret_arr = qsort(arr)
    sumcomp += int(ret_arr[0])
    sumswap += int(ret_arr[1])
    print("comparisons: " + str(sumcomp) + " swaps: " + str(sumswap))

def get_returns(func):
    ret_arr = func
    print("comparisons: " + str(ret_arr[0]) + " swaps: " + str(ret_arr[1]))



def compare_sorts(arr):
    qsort_time(arr)
    timsort_time(arr)
    print("\n")
    

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
    t1 = timeit.Timer(lambda: internal_sorting())
    print("INTERNAL SORTINGS TAKES: ",t1.timeit(1))
    
    print("\n")
    
    #external_sorting
    t2 = timeit.Timer(lambda: external_sorting())
    print("EXTERNAL SORTINGS TAKES: ", t2.timeit(1))
    n = 2500
    matrix = []
    for row in range(n):    
        a = []
        for column in range(n):   
            a.append(random.randint(0, n))
        matrix.append(a)

    
        
    print("\n\nсортировка матрицы 2500x2500 TIMSORT")
    timsort_matrix_time(matrix)

    print("\n\nсортировка матрицы 2500x2500 QSORT")
    qsort_matrix_time(matrix)

main()

    