import matplotlib.pyplot as plt
import numpy as np

def conjecturePlot (n) :
    """
    Représente graphiquement l'évolution de la suite de Syracuse 
    pour un certain n
    """
    plt.style.use("bmh")
    y = [n]
    while n > 1 :
        if n%2 : # if n%2==1 (as 1 is True in boolean)
            n = 3*n+1
        else : # if n is pair
            n //= 2
        y.append(n)
    plt.xlabel("Number of iterations")
    plt.ylabel("Value of n")
    plt.title(f"Evolution of Syracuse's suite for n={y[0]}")
    plt.plot (np.arange(len(y)), y)
    plt.show(); return None


if __name__ == '__main__' :
    n = int(input("Enter the starting number : "))
    conjecturePlot(n)