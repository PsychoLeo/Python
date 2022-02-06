def gcd(a, b) :
    while b > 0 :
        a, b = b, a%b
    return a

def findCoef(a, b, d) :
    """
    Trouve un couple (u, v) solution de au + bv = d
    Renvoie None s'il n'en existe pas
    """
    g = gcd(a, b)
    # On résout d'abord au + bv = PGCD(a, b)
    # On multiplie la solution particulière par d//PGCD(a, b)
    if b > a : # on fait de sorte que a >= b
        a, b = b, a
    (uPart, vPart, g) = solvePart(a, b)
    if d % g :
        return None
    return (uPart*(d//g), vPart*(d//g))

def solvePart(a, b) :
    if b == 0 :
        return (0, 1, a)
    # On fait l'algorithme d'Euclide et on remonte
    r = a%b
    q = a-r
    u, v, g = solvePart(b, r)
    return (v, u-q, g)
    

print("Entrer les coefficients entiers positifs a, b, d de l'équation diophantienne au + bv = d : ")
print("Ecrire a, b, d sous la forme : a b d")
a, b, d = list(map(int, input().strip().split()))
print(findCoef(a, b, d))