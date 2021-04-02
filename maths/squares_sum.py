from math import sqrt

def is_square(x):
  return sqrt(x) - int(sqrt(x)) == 0.0

def impossible_square_sum (n) :
    sol = []
    for i in range (n+1) :
        for j in range (n+1) :
            sol.append (i**2 + j**2)
    sol = list(dict.fromkeys(sol))
    sol.sort ()
    print (sol)
    for k in sol :
        if is_square (k) == True :
            sol.remove (k)
    return (sol)


def imp_squares (n) :
    init = [i for i in range (n+1)]
    comp = []
    for j in range (n) :
        for k in range (n) :
            comp.append (j**2 + k**2)
    comp = list (dict.fromkeys(comp))
    comp.sort ()
    print (comp)
    for h in init :
        for i in comp :
            if h**2 == i :
                init.remove (h)
    return init
                
                
# modification in 2020 (my python improved)

# on cherche les nombres différents de c (entiers naturels) tels que a²+b² = c
# (avec a et b des entiers naturels)

def notsumsquares (n):
    
    '''input : n, the value to which the program will execute 
    output : values that are different than c 
    (so that can't be expressed as a sum of 2 squares)'''
    
    sum_squares = set([i**2+j**2 for i in range (n+1) for j in range (n+1)])
    return set([i for i in range (n+1)]) - (sum_squares)
