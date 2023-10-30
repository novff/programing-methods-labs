import csv
import copy
import timeit
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

def main():
#3.2.1 Внешняя сортировка. 
#3.2.2 Внутренняя сортировка. 
    print("ВНУТРЕННЯЯ СОРТИРОВКА")
    #3.2.2.1 объединение
    print("сортировка продукта объединения массивов")
    merged_array = readArray("f1.txt") + readArray("f2.txt")
    qsort_time(merged_array)
    timsort_time(merged_array)
    print("\n")

    #3.2.2.2 перечисление
    print("сортировка продукта перечисления массивов")
    intersection_array = list(set(readArray("f1.txt")).intersection(set(readArray("f2.txt"))))
    qsort_time(intersection_array)
    timsort_time(intersection_array)
    print("\n")

    #3.2.2.3 разность
    print("сортировка продукта разности массивов")
    difference_array = list(set(readArray("f1.txt")).difference(set(readArray("f2.txt"))))
    qsort_time(difference_array)
    timsort_time(difference_array)
    print("\n")

    #3.2.2.4 симметричная разность
    print("сортировка продукта симмтеричной разности массивов")
    symmetric_diff_array = list(set(readArray("f1.txt")).symmetric_difference(set(readArray("f2.txt"))))
    qsort_time(symmetric_diff_array)
    timsort_time(symmetric_diff_array)
    print("\n")
    
main()
    