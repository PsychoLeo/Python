# SORTING LISTS EDX course

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i] # changing minimum value of the list for each value in list
        j = i+1
        while j < len(L):
            if minVal > L[j]: # if value in list is superior to another one in list --> SEARCHING MINIMUM
                minIndx = j
                minVal = L[j] # i becomes j -> minimum value of the list changes
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp # changings first value to minimum found before
            
########################
            
def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1

##########################
            
def mySort(L):
    """ L, list with unique elements """
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)): # 
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

##########################