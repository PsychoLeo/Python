import matplotlib.pyplot as plt

def courbe (n, t, T) :
    x = [i for i in range (0, int(t/T)+1)]
    y = [n]
    temps = 0
    bact = n
    for j in range (1, int(t/T)+1) :
        temps += T
        bact *= 2
        y.append (bact)
    plt.ylabel ('Nombre de bactéries')
    plt.xlabel ('Temps (en périodes T = %s s)' % (T))
    plt.axis ([-0.2, x[-1]+1, 0, y[-1]*11/10])
    plt.title ('Évolution d\'une population de bactéries en fonction du temps')
    plt.plot (x, y, marker = 'o')
    plt.show ()
    
if __name__ == '__main__' :
    n =  int(input("Entrer le nombre de cellules initiales (nombre entier) : "))
    t = int(input("Entrer le temps total laissé aux cellules (en secondes, nombre entier) : "))
    T = int(input("Entrer la période de réplication (en secondes, nombre entier) : "))
    if t < T :
        print ("Si la période est supérieure au temps total laissé aux cellules, il n'y aura pas de réplication.")
    courbe (n, t, T)
    