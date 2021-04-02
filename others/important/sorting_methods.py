import time
import random

def bubbleSort (l) :
    '''
    input : list to sort
    output : sorted list using bubble sort
    Complexity : O(n^2)
    '''
    i, swaps = 0, 0
    while True :
        if i == len(l)-1 :
            if swaps == 0 :
                break
            else :
                swaps, i = 0, 0
        else :
            if l[i] > l[i+1] :
                l[i], l[i+1] = l[i+1], l[i]
                swaps += 1
            i += 1
    return l



def mergeSort (l) :
    '''
    input : unsorted list
    output : sorted list, using merge sort
    Complexity : O(n*log(n))
    '''
    lists = [l[i:i+1] for i in range (len(l))]
    # print(lists)
    while len(lists) > 1 :
        for i in range (0, len(lists)//2):
            lists[i] = fusion(lists[i], lists[i+1])
            del lists[i+1]
    return lists[0]


def fusion(l1, l2):
    """
    Fusion de 2 listes l1 et l2
    """
    l1.append(float("Inf"))
    l2.append(float("Inf"))
    combined_length = len(l1)+len(l2)-2
    result = [0 for _ in range (combined_length)]
    i, j = 0, 0
    for k in range(combined_length):
        if l1[i] < l2[j]:
            result[k] = l1[i]
            i += 1
        else:
            result[k] = l2[j]
            j += 1
    return result


def insertionSort (l) :
    '''input : a list, output : sorted list using insertion sort'''
    for i in range (len(l)) :
        j = i
        while j>0 and l[j] < l[j-1] :
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1
    return l


def getRandomList (size, max_val) :
    return [random.randint(0, max_val) for _ in range (int(size))]

def runBubble ():
    # Bubble sort
    start = time.time()
    sorted_list_bubble = bubbleSort (liste)
    print(f'Time using Bubble sort : {(time.time() - start)*(10**3)} milliseconds')

def runMerge ():
    # Merge sort
    start = time.time()
    sorted_list_merge = mergeSort(liste)
    # print(sorted_list_merge==sorted(liste))
    print(f'Time using Merge sort : {(time.time() - start)*(10**3)} milliseconds')
    # print (sorted_list_merge == sorted(liste)) # check if works

def runInsertion ():
    # Insertion sort
    start = time.time()
    sorted_list_insertion = insertionSort(liste)
    print(f'Time using Insertion sort : {(time.time() - start)*(10**3)} milliseconds')
    # print(sorted_list_insertion == sorted(liste)) # check if works

def runPythonSort () :
    # Python sorted() method
    start = time.time()
    sorted_list_insertion = sorted(liste)
    print(f'Time using Python sorted() method : {(time.time() - start)*(10**3)} milliseconds')
    # print(sorted_list_insertion == sorted(liste)) # check if works

if __name__ == '__main__' :
    list_size = 1000000
    liste = getRandomList(list_size, 100)
    # print (liste)
    print (f'Testing with size {int(list_size)}')
    # runBubble()
    runMerge()
    # runInsertion()
    # runPythonSort()
