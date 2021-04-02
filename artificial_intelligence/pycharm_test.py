import tensorflow
import keras
import matplotlib.pyplot as plt
from sympy import *

'''
x = [i for i in range (10)]
y = [i**2 for i in range (10)]
plt.plot (x, y)
plt.show ()
'''

def sympy_plot (function, limits) :
    x = [i for i in range (limits[0], limits[1])]
    y = [f(i) for i in x]
    plt.plot (x, y)
    plt.show ()
    return None

def f(i) :
    return function.subs({x:i})

def hello (name) :
    return 'hello ' + name

if __name__ == '__main__' :
    x = Symbol ('x')
    function = input ('Enter the function : f(x) = ')
    function = sympify (function) 
    limits = input ('Enter the limits of the function plotting (list) : ')
    sympy_plot (function, eval(limits))
