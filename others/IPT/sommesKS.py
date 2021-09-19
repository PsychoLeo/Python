from math import sqrt
import time

def somme_ks (n) :
    k = 0
    SommeDesK = 0
    while k+k**2+k**3<n+1 :
        SommeDesK += k
        k += 1
    return SommeDesK

def getDivOpti(n): # complexité O(sqrt(n))
    div = []
    for i in range (1, int(sqrt(n))+1) :
        if n % i == 0 :
            div.append(i)
            if n // i != i :
                div.append(n//i)
    return div


def getDiv(n) : # complexité O(n)
    diviseursDeN = []
    for i in range (1, n+1) :
        if n%i == 0 :
            diviseursDeN.append(i)
    return diviseursDeN

if __name__ == '__main__': 
    n = 100*1000*1000
    t = time.time()
    l1 = getDiv(n)
    print(f"Programme moins Opti : {time.time()-t} seconds")
    t = time.time()
    l2 = getDivOpti(n)
    print(f"Programme Leo : {time.time()-t} seconds")