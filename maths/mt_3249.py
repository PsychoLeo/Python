for mod in range (2, 25) :
    print(f"Modulo {mod}")
    for n in range (1, 100) :
        r = 2**(n-1)*n+1
        print(r% mod)
    input()