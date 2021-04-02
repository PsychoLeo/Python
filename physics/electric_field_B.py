### Création de cartes de champ électrostatique
### créé par une ou deux particules chargées
### (Seules la direction et le sens sont affichés)

import numpy as np
import matplotlib.pylab as plt

### Constantes du problème
xmin, ymin, xmax, ymax = -2, -2, 2.125, 2.125  # Taille de la zone en m
h = 0.25  # Pas de la zone en m
K = 8.99E9  # Constante de Coulomb en USI
e = 1.60E-19  # Charge élémentaire en C


class Particule():
    particules = []
    Location_part = [[], []]  # Liste des coordonnées de toutes les particules

    def __init__(self, q, x_particule, y_particule):
        self.q = q  # Charge
        self.positif = q >= 0 # Si la charge est positive ou non
        self.x = x_particule  # Abscisse
        self.y = y_particule  # Ordonnée
        if self.positif:      # Si POSITIF
            Particule.Location_part[1].append((self.x, self.y))
        else:   # Si NEGATIF
            Particule.Location_part[0].append((self.x, self.y))

        self.r = self.distance(x_champ_tot, y_champ_tot)  # Distances par rapport aux points du graphique
        # Loi de Coulomb pour obtenir les coordonnées radiales du champ E
        self.E = []
        for row in self.r:
            self.E.append([K * self.q / (dist ** 2)
                           if dist != 0
                           else None
                           for dist in row])
        self.E = np.array(self.E, dtype=np.float64)
            # Cordonnées en vecteur unitaire de la paricule
        listCoupleRX = np.array([list(zip(rowR, rowX)) for rowR, rowX in zip(self.r, x_champ_tot)])
        listCoupleRY = np.array([list(zip(rowR, rowY)) for rowR, rowY in zip(self.r, y_champ_tot)])

        self.ux = []  # X
        for row in listCoupleRX:
            self.ux.append([(absc - self.x) / dist if dist != 0 else None for dist, absc in row])
        self.ux = np.array(self.ux, dtype=np.float64)

        self.uy = []  # Y
        for row in listCoupleRY:
            self.uy.append([(ordo - self.y) / dist if dist != 0 else None for dist, ordo in row])
        self.uy = np.array(self.uy, dtype=np.float64)  # Shape = (17,17)

        self.Ex = self.E * self.ux  # Coordonnées cartésiennes champ E1
        self.Ey = self.E * self.uy
        Particule.particules.append(self)  # On l'ajoute à la liste des particules
        # print("r", self.r[8, 3])
        # print("x", x_champ_tot[8, 3])
        # print("y", y_champ_tot[8, 3])
        # print("E", self.E[8, 3])
        # print("Ex", self.Ex[8, 3])
        # print("Ey", self.Ey[8, 3])

    def distance(self, x, y):
        """
        Renvoie la distance de la particule par rapport à x et y
        :param x: abcisse d'un point
        :param y: ordonnée de ce point
        :return: distance par rapport à la particule
        """
        return ((x - self.x) ** 2 + (y - self.y) ** 2) ** 0.5  # Théorème de Pythagore

    def __repr__(self):
        return "Charge :"+str(self.q/e)+' e\n' + "Location: \n" + "----Abscisse: " + str(self.x) + " m\n----Ordonnée: "+ str(self.y) + " m"


### Coordonnées (x,y) de tous les points de calcul
XX = np.arange(xmin, xmax, h)
YY = np.arange(ymin, ymax, h)
x_champ_tot, y_champ_tot = np.meshgrid(XX, YY)  # Return coordinate matrices from coordinate vectors.

# PARTICULES
Particule(e, -2, 0)
Particule(e, 2, 0)
Particule(-e, 0, -2)
Particule(-e, 0, 2)
Particule(e, 0, 0)

### Coordonnées du champ E
Ex_champ_tot = np.array(sum(
    [particule.Ex for particule in Particule.particules]))  # Calcul de l'abscisse x du vecteur du champ électrostatique
Ey_champ_tot = np.array(sum(
    [particule.Ey for particule in Particule.particules]))  # Calcul de l'ordonnée y du vecteur du champ électrostatique
# print("Ex_tot:", Ex_champ_tot[8,3])
# print("Ey_tot:", Ey_champ_tot[8,3])

### Norme des vecteurs E
E_champ_tot = (Ex_champ_tot ** 2 + Ey_champ_tot ** 2) ** 0.5

### vecteur E normalisé
### (pour avoir des flèches de taille identique)
Ex_champ_tot = Ex_champ_tot / E_champ_tot
Ey_champ_tot = Ey_champ_tot / E_champ_tot

### Tracé des vecteurs normalisés
plt.rcParams['axes.formatter.use_locale'] = True
plt.figure(1, figsize=(5, 6))
plt.quiver(x_champ_tot, y_champ_tot, Ex_champ_tot, Ey_champ_tot, E_champ_tot, cmap='jet')
plt.colorbar(orientation="horizontal")
plt.plot(list(list(zip(*Particule.Location_part[1]))[0]), list(list(zip(*Particule.Location_part[1]))[1]), "k.", label="Particule positive")
plt.plot(list(list(zip(*Particule.Location_part[0]))[0]), list(list(zip(*Particule.Location_part[0]))[1]), "b.", label="Particule négative")
plt.legend(loc='upper right')
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Directions et sens du champ électrostatique")
plt.show()
# plt.savefig('Figure3.png')