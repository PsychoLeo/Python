from pylab import *

print("**********************")
print("*   Lancer de poids  *")
print("* Exercice 54 p. 336 *")
print("*********Hatier 2020**")

### NE PAS MODIFIER
m=4.0   #Masse du systeme (en kg)
g=9.81  #Norme du champ de pesanteur (en N/kg)
k=0.1   #Coefficient de frottement (en N.s/m)
Tx=-10  #Force due au vent horizontal (en N)
Dt=1E-2 #Pas de temps en seconde
v0=10   #Norme de la vitesse initiale au moment du lancer (en m/s)
h=2.2   #Altitude du la boule au moment du lancer (en m)
angle=40 #Angle de tir (en °)

# Initialisations
t=[0]
x=[0]
y=[h]
vx=[v0*cos(angle/180*pi)]
vy=[v0*sin(angle/180*pi)]
p=0

# BOUCLE calculant le mouvement
while y[p]>=0:
    t.append(t[-1]+Dt)
    #Coordonnees de la somme des forces
    Fx=-k*vx[p]+Tx  
    Fy=-m*g-k*vy[p]

##### A COMMENTER exercice 54 question a #####
    #Coordonnees du vecteur vitesse a l'instant t + Dt 
    vx.append(vx[p]+Fx*Dt/m)
    vy.append(vy[p]+Fy*Dt/m)
    #Coordonnees du vecteur position a l'instant t + Dt
    x.append(x[p]+vx[p]*Dt)
    y.append(y[p]+vy[p]*Dt)

##### NE PAS MODIFIER
    p=p+1
    
#### A COMPLEETER exercice 54 question c #####
portee= round(x[-1], 3) # Expression de la portee

print("Pour l'angle ",angle,'° la portee du tir est ',portee,' m')  

# Trace de la trajectoire du système
plot(x,y)
xlabel("x (en m)")
ylabel("y (en m)")
xlim(0,1.1*max(x))
ylim(0,1.1*max(y))
title("Trajectoire")
grid(True)
show()
