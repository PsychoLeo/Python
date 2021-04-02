import numpy as np
import matplotlib.pyplot as plt
import random

#### Plotting simulation of n dices throw ####

def dice (n_dices, n_throws) :
    for i in range (n_throws) :
        val = 0
        for j in range (n_dices) :
            val += random.randint (1, 6)
        y[val] += 1
    return [round((i/n_throws), 3) for i in y.values()]

if __name__ == '__main__' :
    n_dices = int(input('Enter the number of dices to roll at each throw : '))
    n_throws = int(input('Enter the number of throws : '))
    x = list(range(n_dices, n_dices*6+1))
    y = {i: 0 for i in x}
    plt.style.use('seaborn')
    # plt.hist(dice(n_dices, n_throws), bins = x, edgecolor = 'k')
    plt.xlabel (f'Score for {n_dices} dices')
    plt.ylabel ('Probability')
    plt.bar (x, dice(n_dices, n_throws))
    plt.show ()