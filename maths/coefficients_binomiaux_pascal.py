import pprint

def pascal (rows):
    assert rows >= 1, 'Number has to be superior or equal to 1'
    triangle = [[1]]
    for i in range (1, rows+1):
        triangle.append ([1]+[triangle[-1][j]+triangle[-1][j-1] for j in range (1, i)]+[1])
    pprint.pprint(triangle)
    return None

def pascal_returning (rows):
    assert rows >= 0, 'Number has to be superior or equal to 0'
    if rows == 0:
        return []
    triangle = [[1]]
    for i in range(1, rows + 1):
        triangle.append([1] + [triangle[-1][j] + triangle[-1][j - 1] for j in range(1, i)] + [1])
    return triangle

def parmi_pascal (k, n): # calcul de k parmi n
    return pascal_returning(n)[n][k]

def parmi (k, n) :
    return factoriel(n)//(factoriel(k)*factoriel(n-k))

def factoriel (n, k=1):
    return k if n==0 or n==1 else factoriel(n-1, k*n)

