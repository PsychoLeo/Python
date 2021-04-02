from math import exp

# Codé par Hubert LEROUX & Léopold BERNARD ®

def eulerMethod(n,d = 1000):
    """
    Renvoie la valeur de exp(n)
    """
    if n < 0: # par définition : e^(-n) = 1/(e^n)
        # mouvement illégal : on utilise des propriétés de e^n avant de la définir :(
        return 1/(eulerMethod(-n, d))
    # ON commence en sachant que exp(0)=1
    x = 0
    y = 1
    while x < n:
        y=y*(1+1/d)
        x+=1/d
    # Ceci revient à faire (1+1/d)^(d*n) = ((1+1/d)^d)^n = e^n
    # On retrouve la formule lim (n->+inf) de (1+1/n)^n = e
    # Trop stylé !
    return y 

def artithmeticMethodWithExpoRapide(x, precision=50):
    """
    On implémente ici la limite vu en cours:
    exp(x) = lim(n->+inf) de (1+x/n)^n
    ici n = 2^precision
    """
    assert precision <= 50, "La précision doit être inférieure ou égale à 50, au delà les nombres sont trop grands"
    y = (1+x/(1<<precision))
    for _ in range(precision):
        y = y * y 
    return y



N = 1
print(f"Bibliothèque mathématique de l'ordinateur : exp(n) = {exp(N)}")
print(f"Méthode d'Euler implémentée : {eulerMethod(N)}")
print(f"Méthode d'exponentiation rapide : {artithmeticMethodWithExpoRapide(N)}")



