def factA (n) :
    if n in [0,1] :
        return 1
    else :
        return n*fact(n-1)

def fact(n, val=1) :
    return val if n in [0,1] else fact(n-1, n*val)

# factB = lambda n, val=1 : val if n in [0,1] else fact(n-1, n*val)