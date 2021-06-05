MAX = 10*1000*1000

def gcd(a, b) :
    return a if b == 0 else gcd(b, a%b)

def fillPrimes() :
    P[0] = P[1] = False
    for i in range (2, MAX) :
        if P[i] :
            if i > 5 :
                primes.append(i)
            for j in range (i*i, MAX, i) :
                P[j] = False

def pow2mod(pow2) :
    r = 2**pow2
    p = list(range(r))
    print("p : ", *p)
    print("p^8-1 :", *[(i**8-1)%r for i in p])

def main():
    # P = [True]*MAX
    # primes = []
    # fillPrimes()
    # # print(primes)
    # pgcd = gcd(primes[0]**8-1, primes[1]**8-1)
    # for i in range (2, len(primes)) :
    #     pgcd = gcd(pgcd, primes[i]**8-1)
    # print(pgcd)
    for i in range (1, 7) :
        print()
        pow2mod(i)

main()