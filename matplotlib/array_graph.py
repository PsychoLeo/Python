import matplotlib.pyplot as plt
from sympy import *

size = 7 # size of the graph (7 is the max - value recommended : between 5 and 7)
# for the moment, keep 'size' at its original value (size = 7)

def array_graph(f):
    '''input : a function f(x) as a string
    output : a plot on an array from x = -5 to x = 5'''
    global size
    assert size <= 7 and isinstance(size, int), 'graph is too big / size has to be an integer'
    x = Symbol('x')

    xvals = list(range(-size, size + 1))
    f = sympify(f)
    yvals = [round(f.subs({x: i})) for i in xvals]
    res = [['|' if i == size else '.' for i in range(size * 2 + 1)] for j in range(size * 2)]
    res [size] = ['_' for i in range (size*2+1)]

    # modify this part of the code
    for x in range(len(yvals)):
        if yvals[x] < size and yvals[x] >= -size:
            res[yvals[x]+size][x] = 'X'
    from pprint import pprint
    pprint(res[::-1])
    return None


if __name__ == '__main__' :
    print ('Enter the function you want to plot using array plotting')
    f = input ('f(x) = ')
    print ()
    print ('Graphical representation of f(x) = {0} on [{1} ; {2}]' .format (f, -size, size))
    array_graph (f)