import matplotlib.pyplot as plt
import random as rd
import sys

"""
Attention : il faut que tu ailles dans ton terminal et que tu entres :
pip install matplotlib
OU SINON tu vas sur le site de matplotlib (tu cherches) et tu l'installes
"""

def lancerDes (numDes, numLancers):
    """
    numDes : nombre de dés lancés par lancer (1, 2, 3, ...)
    numLancers : nombre de lancers de uniques/ paires/ triplets... de dés
    Renvoie une courbe du nombre de lancers de dés
    """
    # assert numDes > 0 and isinstance(numDes, int), "Nombre de dés est invalide"
    # assert numLancers > 0 and isinstance(numLancers, int), "Nombre de lancers est invalide"
    plt.style.use('seaborn') # effet stylistique pour le graphe
    y = {i:0 for i in range(numDes, 6*numDes+1)}
    for i in range (numLancers) :
        scoreActuel = sum([rd.randint(1, 6) for k in range (numDes)])
        y[scoreActuel] += 1
    plt.bar(y.keys(), y.values())
    plt.xlabel(f'Score du lancer de {numDes} dés')
    plt.ylabel(f'Nombre de lancers')
    plt.show()

if __name__ == '__main__' :
    while True : 
        try : 
            numDes = int(input("Entrer le nombre de dés lancés par lancer (1, 2, 3, ...) : "))
            numLancers = int(input(f"Entrer le nombre de lancers de {numDes} dés : "))
            break
        except ValueError:
            print("Nombre de dés/ nombre de lancers est invalide")
    lancerDes(numDes, numLancers)