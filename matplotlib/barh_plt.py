import random
import matplotlib.pyplot as plt


def random_bars(n):
    x = [i for i in range(n)]
    y = [random.random() for i in range(n)]
    med_y = sum(y) / len(y)
    plt.barh(x, y, align='center')
    plt.yticks()
    plt.ylabel('Random numbers')
    plt.xlabel('Value of the random number')
    plt.axis([0, 1, None, len(y)])
    plt.grid()
    plt.show()


if __name__ == '__main__':
    n = int(input('Entrer le nombre de valeurs aléatoires que vous voulez représenter : '))
    random_bars(n)
