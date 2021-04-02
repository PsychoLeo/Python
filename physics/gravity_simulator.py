from vpython import scene, vector, sphere, mag, norm, rate, keysdown
import sys

freq = 100 # 100 calculs par secondes
dt = 60*2 # DetlaT eb secondes entre chaque calculs
t = 0 # initialisation du temps
G = 6.667e-11
scene.x, scene.y = 250, 80  # centering the window (optimized for SXGA displays)
scene.width, scene.height = 1200, 600


class Obj():
    """
    Object in space
    """
    objects = []


    def __init__(self, pos, mass, v, radius, args):
        """
        Create an object
        param: pos is a tuple of the position
        param: mass is the mass in kg of the obj
        param: v is a tuple of its velocity
        """
        self.sph = sphere(pos=vector(pos[0], pos[1], pos[2]), radius=radius, velocity=vector(v[0], v[1], v[2]), **args)
        self.dv = 0
        self.mass = mass
        Obj.objects.append(self)

    def move(self):
        self.sph.velocity += self.dv 
        self.sph.pos += self.sph.velocity*dt # On déplace l'objet

    def calcule(self):
        """
        Calcule dv, la variation de vitesse due à la somme des forces subies
        """
        somme_forces = vector(0,0,0)
        self.dv = 0
        for obj in Obj.objects: # Pour tous les objets de l'espace
            if obj == self: # Si cet objet en question est le mâme que celui qu'on étudie
                pass
            else: # Sinon
                somme_forces = somme_forces + force_grav(obj, self) # On ajoute à la somme des forces la force gravitationnelle du à obj sur self, l'objet qu'on étudie
        self.dv = (somme_forces*dt)/self.mass # clacul de dv


def force_grav(A,B):
    """
    Renvoie un vecteur de la force exercé par A sur B
    """
    d = mag(A.sph.pos - B.sph.pos) # distance entre les deux objets
    u = norm(A.sph.pos - B.sph.pos) # vecteur unitaire entre les deux objets
    F = u*((G* A.mass * B.mass)/(d**2)) # Calcul de F, le force gravitationnelle entre les deux objets
    return F


def main():
    """
    Fonction principale d'animation
    """
    global t
    while True:
        for obj in Obj.objects: # Pour tous les objets existants
            obj.calcule() # On calcule la variation de vitesse
        for obj in Obj.objects:
            obj.move() # Déplace les astres dans le ciel

        t += dt # Avancement du temps

        # Retard artificiel pour l'animation
        rate(freq)

        # Affichage du temps
        if t%(3600*24)==0: # Si un jour passe:
            print(str(t/(3600*24))+' jours') 
        
        k = keysdown()
        if 'esc' in k:
            print("Fin annimation")
            break
    exit()
    sys.exit("Fin du programme")

    


#? ======== 3 CORPS ============
# TERRE = Obj((0,0,0), 5.972e25, (-1e3,1e3,-5e2), 6.370e6, {"color": vector(0.1,0.1,1), "make_trail":True})
# LUNE = Obj((2e8,0,0), 7.3477e22, (1e2,1e3,4.5e3), 3e6, {"color" : vector(1,1,1), "make_trail":True})
# LAMBDA = Obj((-1e8,0,0), 10e22, (0,1e3,-5e3), 3e6, {"color" : vector(0,1,0), "make_trail":True})

#? ======== CHAOS ============
TERRE = Obj((0,0,0), 5.972e25, (-1e3,1e3,-5e2), 6.370e6, {"color": vector(0.1,0.1,1), "make_trail":True})
LUNE = Obj((2e8,0,0), 7.3477e22, (1e2,1e3,4.5e3), 3e6, {"color" : vector(1,1,1), "make_trail":True})
LAMBD1 = Obj((-1e8,0,0), 10e22, (0,1e3,+5e3), 3e6, {"color" : vector(0,1,0), "make_trail":True})
LAMBD2 = Obj((5e7,0,0), 10e20, (0,1e3,-5e3), 5e5, {"color" : vector(1,0,0), "make_trail":True})

#? ======================Système Solaire =======================
# soleil = Obj((0,0,0), 1e30, (0,0,0), 1e5, {"color" : vector(1,0,0), "make_trail":True})
# terre = Obj((1e6,0,0), 1e3, (10,100,0), 2.5e4, {"color" : vector(0,0,1), "make_trail":True})
# lune = Obj((1.50e11+3.84e8,0,0), 7.3477e22, (0,1e4,0), 1.74e6, {"color" : vector(1,1,1), "make_trail":True})

#? =================== TERRE - LUNE =====================
# TERRE = Obj((0,0,0), 5.972e25, (1e2,0,0), 6.370e6, {"color": vector(0.1,0.1,1), "make_trail":True})
# LUNE = Obj((2e8,0,0), 7.3477e22, (0,0,4.5e3), 3e6, {"color" : vector(1,1,1), "make_trail":True})
# LAMBDA = Obj((-1e8,0,0), 10e22, (0,0,5e3), 3e6, {"color" : vector(0,1,0), "make_trail":True})

if __name__ == "__main__":
    main()