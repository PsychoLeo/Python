def frange (start, final, increment) :
    numbers = []
    while start < final :
        numbers.append (start)
        start += increment
    return numbers

from matplotlib import pyplot as plt
import math

def draw_graph (x, y) :
    plt.plot (x, y)
    plt.xlabel ('x-coordinate')
    plt.ylabel ('y-coordinate')
    plt.title ('Projectile motion of a ball')
    
def frange (start, final, interval) :
    numbers = []
    while start < final :
        numbers.append (start)
        start += interval
    return numbers

def draw_trajectory (u, theta) :
    theta = math.radians (theta)
    g = 9.81
    
    t_flight = 2*u*math.sin(theta)/g
    intervals = frange (0, t_flight, 0.004)
    
    x = []
    y = []
    for t in intervals :
        x.append (u*math.cos(theta)*t)
        y.append (u*math.sin(theta)*t - 0.5*g*t**2)
    
    draw_graph (x, y)

if __name__ == '__main__' :
    theta_list = [20, 50, 70]
    u = 25 # float(input('Enter the initial velocity : '))
# theta = float(input('Enter the angle of projection (degrees) : '))
    for theta in theta_list :
        draw_trajectory (u, theta)
    plt.legend (['20', '50', '70'])
    plt.show ()