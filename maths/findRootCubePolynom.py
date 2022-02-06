def findRoot(a, b, c, d) :
    """
    Trouve une racine d'un polynôme de degré 3
    Complexité O(log(n)) -> par dichotomie
    """
    left, right = -1, 1
    sg = signe(a)
    while sg*p(left) >= 0 :
        left <<= 1
    while sg*p(right) <= 0 :
        right <<= 1
    r = (left+right)/2
    val = p(r)
    while abs(val) > precision :
        if val < 0 :
            if sg > 0 :
                left = r
            else :
                right = r
        else :
            if sg > 0 :
                right = r
            else :
               left = r
        r = (left+right)/2
        val = p(r)
    return r

def signe(a) :
    return -1 if a < 0 else 1
        
def p(x) :
    return a*(x**3) + b*(x**2) + c*x + d

if __name__ == "__main__" :
    # a, b, c, d = map(int, input().split())
    a, b, c, d = 1, -18, 115, -391
    precision = 1e-6
    r = findRoot(a, b, c, d)
    print(r)