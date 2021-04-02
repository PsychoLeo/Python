import random as rd
import sys

def write(txt) :
    sys.stdout.write(txt)

def printArr (arr) :
    """Print out 2D arrays"""
    write('[', end= arr[0])
    for i in range (1, len(arr)-1) :
        print (arr[i])
    print (arr[-1], end= ']')
    return None

def genArr (numRows, numCols, maxVal) :
    return [[rd.randint(0, maxVal) for i in range (numCols)] for _ in range (numRows)]

if __name__ == "__main__" :
    numRows = 15
    numCols = 12 # numbers per row
    maxVal = 1e3
    arr = genArr(numRows, numCols, maxVal)
    printArr(arr)