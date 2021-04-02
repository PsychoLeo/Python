import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

m=4.0   #Masse du systeme (en kg)
g=9.81  #Norme du champ de pesanteur (en N/kg)
k=0.1   #Coefficient de frottement (en N.s/m)
Tx=-10  #Force due au vent horizontal (en N)
Dt=1E-2 #Pas de temps en seconde
v0=10   #Norme de la vitesse initiale au moment du lancer (en m/s)
h=2.2   #Altitude du la boule au moment du lancer (en m)
angle=40 #Angle de tir (en °)

### Initializing variables ###
t=[0]
x=[0]
y=[h]
vx=[v0*np.cos(angle/180*np.pi)]
vy=[v0*np.sin(angle/180*np.pi)]
p=0

while y[p]>=0:
    t.append(t[-1]+Dt)
    #Coordonnees de la somme des forces
    Fx=-k*vx[p]+Tx  
    Fy=-m*g-k*vy[p]
    #Coordonnees du vecteur vitesse a l'instant t + Dt 
    vx.append(vx[p]+Fx*Dt/m)
    vy.append(vy[p]+Fy*Dt/m)
    #Coordonnees du vecteur position a l'instant t + Dt
    x.append(x[p]+vx[p]*Dt)
    y.append(y[p]+vy[p]*Dt)
    p += 1

def get_arrow(val):
    x = np.cos(val)
    y = np.sin(val)
    vx = np.sin(2*val)
    vy = np.sin(3*val)
    return x, y, vx, vy

quiver = ax.quiver(*get_arrow(0))

def update(val):
    global quiver
    quiver.remove()
    quiver = ax.quiver(*get_arrow(val))

ani = FuncAnimation(fig, update, frames=p, interval=50)
plt.show()