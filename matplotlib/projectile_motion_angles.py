import matplotlib.pyplot as plt
import math

def projectile_motion (u, theta) :
    
    g = 9.81
    theta = math.radians (theta)
    t_max = 2*u*math.sin(theta)/g
    x = []
    y = []    
    
    i = 0.0
    dist = []
    while i <= t_max :
        dist.append (i)
        i += 0.002
    for t in dist :
        x.append (u*math.cos(theta)*t)
        y.append (u*math.sin(theta)*t - (g*t**2)/2)
    
    plt.plot (x,y)
    plt.title ('Simulation of the projectile motion of a ball')
    plt.axis (ymin = 0)

    
if __name__ == '__main__' :
    u = float(input("Enter the initial velocity of the projectile (m/s) : "))
    l = []
    n = int(input("Enter the number of angles you would like to try : "))
    for j in range (n) :
        j = float(input('Enter the value of the angle you want to represent (in degrees) : '))
        l.append (j)
    for i in l :
        projectile_motion (u, i)
    plt.legend ([i for i in l])
    plt.show ()