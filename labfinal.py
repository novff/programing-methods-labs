
import csv
import copy
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

def main():
    #writeArrays()

    #
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


    QS_start_time = datetime.now()
    qsort(QS_array)
    QS_end_time = datetime.now()
    print("Quicksort exec took: {}".format(QS_end_time -  QS_start_time))

    



main()
    