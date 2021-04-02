from sympy import *
from sympy.plotting import plot
import re

MODE = 'isolve' # factors, plot, sum_series, or isolve
x = Symbol('x')
y = Symbol ('y')
n = Symbol ('n')


'''1 : Factor finder'''

def factorize (expr) :
    return factor (expr)

'''2 : graphical equation solver'''

def expr_plot (expr1, expr2) :
    plot1 = solve (expr1, y)[0]
    plot2 = solve (expr2, y)[0]
    print ('The solutions of the system are : ' + str (solve ((expr1, expr2), dict = True)[0]))
    return plot (plot1, plot2)

'''3 : summing a series '''

def sum_series (nth, nterms) :
    return summation (sympify(nth), (n, 1, nterms))

'''4 : solving single variable inequalities '''

def isolve (expr) :
    '''input : single variable inequality
    output : the solutions of it'''
    lhs = expr.lhs # passing every term on one side of the expression
    relation = expr.rel_op # finding the relation operator (>, <, >=, <=)
    if lhs.is_polynomial () :
        p = Poly (lhs, x) # representing the expression as a polynomial
        pprint (solve_poly_inequality (p, relation))
    elif lhs.is_rational_function () and not lhs.is_polynomial ():
        numer, denom = lhs.as_numer_denom ()
        p1 = Poly(numer)
        p2 = Poly(denom)
        pprint (solve_rational_inequalities ([[((p1, p2), relation)]]))
    else :
        pprint (solve_univariate_inequality (expr, x, relational = False))
    return None


if __name__ == '__main__' :
    # see the MODE variable at the beginning of the code
    start = False
    if MODE == 'isolve' :
        while start == False :
            try :
                expr = input ('Enter a single variable mathematical inequation to solve (with x): ')
                op = ['<', '>', '<=', '>=']
                used_op = [i for i in op if i in expr][-1]
                sides = re.split ('[< > <= >=]', expr)
                expr = sides[0] +'-('+ sides[1] + ')' + used_op + '0'
                isolve (sympify(expr))
                start = True
            except :
                print ('Invalid input, please enter a valid input of an inequality')
    elif MODE == 'sum_series' :
        while start == False :
            try :
                nth_term = sympify(input ('Enter the expression want to sum (with x,y and n as the number changing) : '))
                nterms = sympify(input ('Enter the number of terms of that sum : '))
                pprint (sum_series (nth_term, nterms))
                start = True
            except :
                print ('Invalid input for a series sum')
    elif MODE == 'plot' :
        while start == False :
            try :
                expr1 = sympify(input('Enter your first expression in terms of x and y : '))
                expr2 = sympify(input('Enter your second expression in terms of x and y : '))
                expr_plot (expr1, expr2)
                start = True
            except :
                print ('Invalid input, please enter a mathematically valid input')
    elif MODE == 'factors' :
        while start == False :
            try :
                expr = sympify (input('Enter a mathematical expression to simplify (with x): '))
                pprint (factorize (expr))
                start = True
            except : # SympifyError not working
                print ('Please enter a mathematically valid input')
    else :
        print ('Invalid input of a MODE')