def main() :
    mod = 7
    for i in range (1, 10) :
        print((fact(7*i)//(pow(7, i)*fact(i))) % 7)

def fact (n) :
    res = 1
    for i in range (2, n+1) :
        res *= i
    return res

main()
