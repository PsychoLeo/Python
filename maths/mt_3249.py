from math import sqrt

MAX = 1000
f = lambda x: pow(2, x-1)*x+1

def isPerfectSquare(n) :
    sq = int(sqrt(n))
    return sq*sq == n

def main() :
    for i in range (1, MAX+1) :
        a = f(i)
        if isPerfectSquare(a) :
            print(f"n = {i}\t| 2^{i-1} * {i} + 1 = {int(sqrt(a))}^2")

main()