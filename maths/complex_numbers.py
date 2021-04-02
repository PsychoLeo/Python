# from math import sqrt

def number_solutions (a, b, c) : # easy
    '''input : a, b, c the real coefficients of a degree 2 polynomial
    output : the number of solutions of this equation in C'''
    delta = b**2 - 4*a*c
    if delta == 0 :
        return 'One real solution'
    elif delta > 0 :
        return 'Two real solutions'
    else :
        return 'Two complex solutions'


def get_solutions (a, b, c) :
    '''input : a, b, c the real coefficients of a degree two polynomial
    output : the roots of the polynomial'''
    delta = b**2 - 4*a*c
    if delta == 0 :
        print(f'x = {-b/(2*a)}')
    elif delta > 0 :
        print(f'x1 = ({-b}-sqrt({delta}))/{2*a}\nx2 = ({-b}+sqrt({delta}))/{2*a}')
    else :
        print (f'x1 = ({-b}-i*sqrt({-delta}))/{2*a}\nx2 = ({-b}+i*sqrt({-delta}))/{2*a}')
    return None