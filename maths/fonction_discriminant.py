#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
import matplotlib.pyplot as plt

# racines du polynôme

def fonction (a, b, c) :
    delta = b**2 - 4*a*c
    x_0 = -b / (2*a)

    if delta < 0 :
        print ('Ce polynôme n\'a pas de racine.')

    elif delta == 0 :
        print ('Ce polynôme a une racine qui vaut {0:.2f}'.format (x_0))

    elif delta > 0 :
        x_1 = (-b-sqrt(delta)) / (2*a)
        x_2 = (-b+sqrt(delta)) / (2*a)
        print ('Ce polynôme a deux racines qui valent {0:.2f} et {1:.2f}'.format (x_1, x_2))

# représentation graphique

def graph (a, b, c) :
    x = [ i for i in range (-10,11)]
    y = [a*i**2 + b*i + c for i in range (-10, 11)]

    plt.plot (x,y, marker = 'o')
    plt.xlabel ('x')
    plt.ylabel ('y')
    plt.title ('Graphique représentatif de la fonction')
    plt.grid ()
    plt.show ()

if __name__ == '__main__' :
    a = input('Entrer la valeur de a : ')
    b = input('Entrer la valeur de b : ')
    c = input('Entrer la valeur de c : ')
    fonction (float (a), float (b), float (c))
    graph (float (a), float (b), float (c))