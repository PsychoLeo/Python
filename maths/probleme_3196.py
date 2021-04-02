def primes (n) :
    P = [True]*(n+1)
    P[0] = False
    primes = set()
    # P[1] = False # ici on suppose que 1 est un nombre premier pour l'exercice
    for i in range (2, n+1):
        if P[i] :
            primes.add(i)
        for j in range (2*i, n+1, i) :
            P[j] = False
    # print (primes)
    return P, primes

# def main():
#     DIVISOR = 90
#     n = 1e5
#     P, primesList = primes(int(n))
#     for i in primesList :
#         if not P[i%DIVISOR] :
#             print(f"{i} ne fonctionne pas pour d = {DIVISOR}")

def theoremeRestesChinois(a, m) :
    """
    a: liste des operateurs tel que x congru à a_i (mod m_i)
    """
    n = len(a)
    x = 0
    M = 1
    for i in m :
        M *= i
    for i in range (n) :
        _, u, v = bezout(a[i], m[i])
        x += a[i]*(M/m[i])*v
    return int(x)%M

def bezout(a, b):
    u, v, uu, vv=1,0,0,1
    while b:
        q, rr=divmod(a, b)
        a, b=b, rr
        u, uu=uu, u-q*uu
        v, vv=vv, v-q*vv
    return a, u, v

def main() :
    a = [1, 1, 2]
    m = [2, 3, 5]
    prod = 1
    for i in m:
        prod *= i
    x = theoremeRestesChinois(a, m)
    print()
    print (f"x congru à {x} (mod {prod})")

main()