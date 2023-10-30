
import csv
import copy
from timeit import timeit
from qsort import *
from timsort import *
from datetime import datetime


def writeArrays():
    arr1 = []
    arr2 = []
    for a in range(0,5001):
        if a % 2 == 0:
            arr1.append(a)
        else:
            arr2.append(a)
    with open("f1.txt", "w") as f:
        wr = csv.writer(f, delimiter=";")
        wr.writerow(arr1)
    with open("f2.txt", "w") as f:
        wr = csv.writer(f, delimiter=";")
        wr.writerow(arr2)

def readArray(fname):
    rdrArr = []
    with open(fname, "r") as file:
        rdr = csv.reader(file, delimiter=";")
        for a in rdr:
            rdrArr += a
    
    numArr = [int(x) for x in rdrArr]
    return numArr

def qsort_time(arr):
    QS_array = copy.deepcopy(arr) #глубокая копия превентивная мера ассоциации двух массивов с одним отрезком памяти
    start_time = datetime.now()
    qsort(QS_array)
    end_time = datetime.now()
    exec_delta = end_time - start_time 
    print("Quicksort exec took: ", exec_delta)

def timsort_time(arr):
    TS_array = copy.deepcopy(arr) #глубокая копия превентивная мера ассоциации двух массивов с одним отрезком памяти
    start_time = datetime.now()
    timsort(TS_array)
    end_time = datetime.now()
    exec_delta = end_time - start_time
    print("Timsort exec took: ", exec_delta)
    



merged_array = readArray("f1.txt") + readArray("f2.txt")
def main():
#3.2.1. Внешняя сортировка. 
    #3.2.1.1 объединение
    print("сортировка продукта объединения массивов")

    #merged_array += (readArray("f1.txt")) 
    #merged_array += (readArray("f2.txt")) 

    print(timeit('timsort(merged_array)', number=1, globals = globals()))
    #qsort_time(merged_array)
    #timsort_time(merged_array)
    print("\n")

    #3.2.1.2 перечисление
    print("сортировка продукта перечисления массивов")

    #intersection_array = []
    #intersection_array = list(set(readArray("f1.txt")).intersection(set(readArray("f2.txt"))))

    #print(intersection_array)

    #qsort_time(intersection_array)
    #timsort_time(intersection_array)
    print("\n")

    #3.2.1.3 разность

    '''
    TS_array = []
    TS_array += (readArray("f1.txt")) 
    TS_array += (readArray("f2.txt")) 


    TS_start_time = datetime.now()
    timsort(TS_array)
    TS_end_time = datetime.now()
    print("Timsort exec took: {}".format(TS_end_time -  TS_start_time))

    QS_array = []
    QS_array += (readArray("f1.txt")) 
    QS_array += (readArray("f2.txt")) 

'''
main()
    