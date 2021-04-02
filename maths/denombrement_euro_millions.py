import random
# import matplotlib.pyplot as plt

# Programmation probabilité de ne rien gagner avec une grille euro millions

# nombres = range(1, 51)
# etoiles = range(2, 12)

NOMBRE_SIMULATIONS = 10000000
# NUM_TRIES = 5 # utile dans le cas où je laisse courir le programme avec une limite

resultats = []

grille_etoile = set([random.randint(1, 11) for _ in range(2)])
grille_nombres = set([random.randint(1, 50) for _ in range(5)])

while True :
    valide = 0 # nombre de grilles valides
    for i in range (NOMBRE_SIMULATIONS) :
        nombres_bons = 0
        for k in range (5) :
            if random.randint(1, 50) in grille_nombres :
                nombres_bons += 1
                if nombres_bons == 2 :
                    valide += 1
                    break
        if nombres_bons == 1 :
            if random.randint(1, 11) in grille_etoile :
                if random.randint(1, 11) in grille_etoile :
                    valide += 1
    print (100-valide*100/NOMBRE_SIMULATIONS)

    with open('/home/leo/Bureau/Programmation/Python/maths/denombrement_euro_resultat.txt', 'a') as f :
        f.write(str(100-valide*100/NOMBRE_SIMULATIONS)+'\n')

# print (f'Résultats : {resultats}')