import numpy as np
import matplotlib.pyplot as plt 
import time


def randSeed () :
    """
    Generating random seeds using time.time() milliseconds
    """
    return time.time()*1e7%1e7


def pseudo_uniform (size, mult=29389, mod=2**31-1, seed=randSeed()) :
    """
    Pseudo random generator
    https://en.wikipedia.org/wiki/Linear_congruential_generator
    """
    U = np.zeros(size)
    x = (seed*mult+1)%mod
    # U[0] = x/mod
    for i in range (size) :
        x = (x*mult+1)%mod
        U[i] = x/mod
    return U

def randBetween (a, b, size) :
    """
    a, b are floats or integers and a<b
    => returns a random number between a and b
    """
    assert a<b, "a should be inferior to b"
    return a+(b-a)*pseudo_uniform(size)

def plotRandom (y, size) :
    plt.style.use('seaborn')
    # x = np.linspace(0, 1, size)
    plt.hist(y, bins=20, edgecolor='k')
    plt.show()


def ownRandom (a, b, size) :
    """
    Trying to implement my own random generator
    (a, b>0 and a<b)
    """
    res = np.zeros(size)
    assert b-a<1e7, "Invalid input"
    for i in range (size) :
        res[i] = time.time()*1e7%1.5e3/1.5e3
    return a+(b-a)*res # only works for big numbers



if __name__ == "__main__" :
    fromFile = True
    if fromFile :
        size = 10000
        low, high = -4, 15
    else :
        low = float(input("Enter the lower number (float/int) : "))
        high = float(input("Enter the higher number (float/int) : "))
        size = int(input("Enter the number of values to plot (int) : "))
    y = randBetween(low, high, size)
    # y = ownRandom(low, high, size)
    # print (y)
    plotRandom(y, size)