def recuPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = base
    
    if exp == 0 :
        result = 1
    else :
        result = result*iterPower(base, exp-1)
    return result

def iterPower (base, exp) :
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    result = 1
    
    for i in range (1, exp+1) :
        result *= base
    return result