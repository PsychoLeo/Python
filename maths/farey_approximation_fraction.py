def approx_farey (x, n) :
    
    '''input : a floating number between 0 and 1 and the number of iterations
    output : a fraction approximating the value of the number'''
    
    a, b, c, d = 0, 1, 1, 1 # initializing fraction 0/1 and 1/1
    
    for i in range (n) :
        mid = (a+c)/(b+d)
        if x == mid :
            return str(a+c) + ' / ' + str(b+d)
        elif x < mid :
            c += a
            d += b
        else :
            a += c
            b += d
    
    return 'Approximation of ' + str(x) + ' : ' + str(a+c) + ' / ' + str(b+d)


def approxi_farey (x, D) :
    '''input : a floating point number (between 0 and 1) and the maximum denominator
    for the simplified fracion
    output : a fraction approximating the value of the number'''
    
    a, b, c, d = 0, 1, 1, 1 # initializing fraction 0/1 and 1/1
    
    while b < D and d < D :
        mid = (a+c)/(b+d)
        if x == mid :
            return str(a+c) + ' / ' + str(b+d)
        elif x < mid :
            c += a
            d += b
        else :
            a += c
            b += d
    
    if b > D :
        return (c, d)
    else :
        return (a, b)
        
        
# program internet

def farey(x, N):
    a, b = 0, 1
    c, d = 1, 1
    while (b <= N and d <= N):
        mediant = float(a+c)/(b+d)
        if x == mediant:
            if b + d <= N:
                return a+c, b+d
            elif d > b:
                return c, d
            else:
                return a, b
        elif x > mediant:
            a, b = a+c, b+d
        else:
            c, d = a+c, b+d

    if (b > N):
        return c, d
    else:
        return a, b
        
        