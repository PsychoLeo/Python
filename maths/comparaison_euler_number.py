from math import e
import matplotlib.pyplot as plt

def factoriel (k) :
    r = 1
    for i in range (1, k+1) :
        r *= i
    return r

def u(n) :
    return (1+1/n)**n

def v(n) :
    v = 1
    for k in range (1, n+1) :
        v = v+1/factoriel(k)
    return v

def euler_number_comparaison (n) :
    x = [i for i in range (1, n+1)]
    y_bernoulli = [u(i) for i in range (1, n+1)]
    y_euler = [v(i) for i in range (1, n+1)]
    y = [e for i in range (1, n+1)]
    plt.plot (x, y_bernoulli, x, y_euler, x, y)
    plt.legend (['Méthode de Bernoulli', 'Méthode d\'Euler', 'e'])
    plt.show ()
    

if __name__ == '__main__' :
    n = int(input("Entrer le nombre jusque auquel vous souhaitez avoir l'approximation des deux méthodes : "))
    euler_number_comparaison (n)