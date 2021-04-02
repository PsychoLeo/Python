# coding=utf-8

from sympy import Symbol, sympify, solve, factor, pprint
import matplotlib.pyplot as plt
from sympy.plotting import plot
from math import cos, sin, tan

##########################################################


def function_plot(function, limits):
    '''input : a function and its left and right limits for plotting
    output : the graphical representation of that function between the two limits and the
    solution(s) to the equation f(x) = 0 '''

    x = [i for i in range(limits[0], limits[1] + 1)]
    y = [f(i) for i in range(limits[0], limits[1] + 1)]

    plt.plot(x, y)
    plt.grid()
    # plt.xlabel ('x')
    # plt.ylabel ('y')
    plt.title('Représentation graphique de f(x) = %s sur %s' % (function, limits))
    plt.show()

    if factor(function) != function:
        print('')
        print('Forme factorisée : f(x) =', factor(function))

    print('')
    print('Les solutions de l\'équation f(x) = 0 sont :')
    for i in range(len(solve(function))):
        print('x =', solve(function)[i])


def f(i):
    '''input : a number
    output : the image of that number by f'''
    return function.subs({x: i})

##########################################################
# x = Symbol('x')
# function = sympify(input('f(x) = '))

# if __name__ == '__main__':
#
#     print('Enter a function')
#
#     limits = [int(input('Enter the inferior limit of the function (integer): ')),
#               int(input('Enter the superior limit of the function (integer): '))]
#
#     function_plot(function, limits)

##########################################################
# more efficient, less nice

def sympy_function_plot(function, limits):

    plot(function, (x, limits[0], limits[1]), xlabel='x', ylabel='f(x)',
         title='Représentation graphique de f(x) = %s sur %s' % (function, limits))

    print('')
    print('Les solutions de l\'équation f(x) = 0 sont :')
    pprint(solve(function, x, dict=True))


def plotting(functions, lims):
    plt.style.use('seaborn')
    x = [i for i in range(lims[0], lims[1] + 1)]
    for num in range (len(functions)):
        y = [eval(functions[num].replace('x', f'({i})')) for i in x]
        plt.plot(x, y, label=f'f{num}')
    plt.legend(loc='upper left')
    plt.show()

if __name__ == '__main__':
    functions = []
    nfuncs = int(input('Enter the number of functions you would like to plot: '))
    assert isinstance(nfuncs, int) and nfuncs > 0, 'Invalid number of functions'
    while True:
        try:
            lims = eval(input('Enter the plotting limits of your function as a list: '))
            break
        except:
            print('Invalid input, please try again.')
    for i in range(nfuncs):
        f = input(f'f{i}(x)= ')
        functions.append(f)
    plotting(functions, lims)