from itertools import combinations
import time

cartes = set([str(i) for i in range(7, 11)] + ['J', 'Q', 'K', 'A'])
couleurs = {'S', 'H', 'D', 'C'}  # anglais pour ne pas avoir des doubles lettres
# spades, hearts, diamonds, clubs

deck = set([couleur + carte for carte in cartes for couleur in couleurs])
possibilities = set(combinations(deck, 5))
print(possibilities)


def unePaire(possibilities):
    '''returning the number of hands possible with only 1 pair'''
    new = []
    num_valides = 0
    for i in possibilities:  # getting to every 5 cards hand
        colors = [i[0] for i in possibilities]
        num_paires = 0
        for i in colors:
            if colors.count(i) == 2:
                num_paires += 0.5
            elif colors.count(i) >= 3:
                break
        if num_paires == 1:
            num_valides += 1
    return num_valides


def deuxPaires(deck):
    pass


if __name__ == '__main__':
    start = time.time()
    print(unePaire(possibilities))
    print(f'Time : {time.time() - start} seconds')
