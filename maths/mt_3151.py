from math import sqrt

MAX = 100
f = lambda p: p**3+8*p+2

def main() :
    for i in range (1, MAX+1, 2) :
        if not isPrime(f(i)):
            print(f"f({i}) = {f(i)} non premier\n\tDiviseurs de p : {' '.join(map(str, findDiv(i)))}\n\tDiviseurs de p^2+8 : {' '.join(map(str, findDiv(i**2+8)))}\n")

def findDiv(n) :
    div = []
    for i in range (2, int(sqrt(n))+1) :
        if n % i == 0 :
            div.append(i)
            if n//i != i :
                div.append(n//i)
    div.sort()
    return div


def isPrime (n) :
    if n < 2 :
        return False
    for i in range (2, int(sqrt(n))+1) :
        if n % i == 0 :
            return False
    return True

main()