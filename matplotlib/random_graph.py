import random
import matplotlib.pyplot as plt

def lancer_des (n) :
    l = []
    x = [i for i in range (1, 7)]
    y = []
    for i in range (1, n) :
        l.append (random.randint (1, 6))
    for b in range (1, 7) :
        y.append (l.count(b)/len(l))
    plt.barh (x, y, align = 'center')
    plt.title ('Probability of getting each number of a dice rolling for %s rolls' % (n))
    plt.show ()

if __name__ == '__main__' :
    n = int(input("Entrer le nombre de lancers de dés que vous souhaitez simuler : "))
    lancer_des (n)