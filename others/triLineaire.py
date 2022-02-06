from random import randint

def sortLin(l) :
    ind = [0]*(maxint+1)
    for i in l :
        ind[i] += 1
    newL = []
    for i in range (len(ind)) :
        for j in range (ind[i]) :
            newL.append(i)
    return newL
    
    
if __name__ == "__main__" :
    maxint = 100
    longueur = 10
    l = [randint(1, maxint) for _ in range (longueur)]
    print(l)
    sortedL = sortLin(l)
    print(sortedL)