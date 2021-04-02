from sympy import Symbol, pprint, init_printing

def series_xpowern_overn (n) :
    
    ''' input : the number to which the function will execute
    output : the series of (x^n / n) printed out using sympy '''
    
    init_printing (order = 'rev-lex') # rev-lex means we can print these series from x up to x^n / n
    
    assert n >= 0 and isinstance (n, int) == True, 'please enter a valid input' # avoid input errors
    
    x = Symbol ('x')
    expr = 0
    
    for i in range (1, n+1) :
        expr += x**i / i

    pprint (expr)
    return expr

def result (n, a) :
    expr = series_xpowern_overn (n)
    x = Symbol ('x')
    return expr.subs ({x:a})

if __name__ == "__main__" :
    n = int(input("Enter n value : "))
    a = int(input("Enter n value to calculate the sum : "))
    # series_xpowern_overn(n)
    print (f"Result (with n = {n}) : {result(n, a)}")