def main() :
    s = 1
    for i in range (6, 51) :
        s *= i
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    decomp = {i:0 for i in primes}
    i = 0
    while s > 1 :
        if s % primes[i] == 0 :
            decomp[primes[i]] += 1
            s //= primes[i]
        else :
            i += 1
    print("$k\cdot k' = "+"\cdot".join([str(p)+"^{"+str(decomp[p])+"}" for p in decomp])+"$")

main()