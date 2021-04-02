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
        i += 0.01
    for t in dist :
        x.append (u*math.cos(theta)*t)
        y.append (u*math.sin(theta)*t - (g*t**2)/2)
    
    plt.plot (x,y)
    plt.title ('Simulation of the projectile motion of a ball')
    plt.axis (ymin = 0)
    plt.show ()

'''def other_values_angles (n) :
    l = []
    for j in range (n) :
        j = float(input('Enter the value of the angle you want to represent (in degrees) : '))
        l.append (j)
    for i in l :
        projectile_motion (u, math.radians (i)) '''
        

if __name__ == '__main__' :
    try :
        u = float(input("Enter the initial velocity of the projectile (m/s) : "))
        theta = float(input("Enter the value (degrees) of the throwing angle : "))
    except ValueError :
        print ('Please enter a valid number')
    else :
        projectile_motion (u, theta)