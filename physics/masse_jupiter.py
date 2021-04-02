from math import log
import matplotlib.pyplot as plt

# informations sur les satellites naturels de Jupiter
periodes = [0.295, 0.298, 0.498, 0.675, 1.769, 3.551, 7.155, 16.689,
            130.02, 240.92, 251.73]
demi_grand_axes = [1.28e5, 1.29e5, 1.814e5, 2.219e5, 4.218e5, 6.711e5, 1.07e6,
                   1.883e6, 7.284e6, 1.117e7 ,1.146e7]
noms = ['Métis', 'Adrastée', 'Amalthée', 'Thébé', 'Io', 'Europe',
        'Ganymède', 'Callisto', 'Thémisto', 'Léda', 'Himalia']

assert len(periodes) == len(demi_grand_axes) == len(noms), 'Listes ne sont pas de même longueur'
nombre_planetes = len(periodes)

def plot (x, y):
    x = [log(i) for i in x]
    y = [log(i) for i in y]
    # x = [(a*1000)**3 for a in x]
    # y = [(T*24*60*60)**2 for T in y]
    for i in range (nombre_planetes) :
        plt.scatter(x, y, cmap='viridis')
        plt.annotate(noms[i], (x[i], y[i]))
    plt.show()

if __name__ == '__main__' :
    plt.style.use('seaborn')
    plt.xlabel('ln(a)')
    plt.ylabel('ln(T)')
    plot (demi_grand_axes, periodes)