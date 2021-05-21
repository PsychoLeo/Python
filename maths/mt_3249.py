from math import sqrt

MAX = 100
squares = set()
f = lambda x: pow(2, x-1)*x+1

def main() :
    for i in range (1, MAX+1) :
        a = f(i)
        if sqrt(a).is_integer():
            print(f"n = {i}\t| 2^{i-1} * {i} + 1 = {int(sqrt(a))}")

main()