import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import cos, sin, pi
from time import sleep

plt.style.use('ggplot')
plt.xlabel('time (s)')
plt.ylabel ('height (m)')

### Getting user input - constants and initial values
g = 9.81
'''
v0 = float(input('Enter the initial velocity (m/s) : '))
alpha = float(input('Enter the initial throw angle (in degrees) : ')) * pi/180
m = float(input('Enter the mass of your system (in kg) : '))
'''
# Test values :
v0, alpha, m = 8, pi/4, 5
tmax = sin(alpha)*v0/g
list_frames = np.linspace(0, tmax, 100)
plt.xlim (-1, tmax+1)

### Defining coordinates of position and speed
position = [[0, 0]]
speed = [cos(alpha)*v0, sin(alpha)*v0]
index = 0

### Animating the object
while position[-1][-1] >= 0 :
    t = list_frames[index]
    position.append([cos(alpha)*v0*t, -g*t**2+sin(alpha)*v0*t])
    speed = [cos(alpha) * v0, sin(alpha) * v0 - g * t]
    # Plotting all vectors and curves
    plt.plot(position, 'r--')
    plt.quiver (position[-1][0], position[-1][-1], speed[0], speed[1])
    index += 1
    sleep(0.5)
    plt.show() ; plt.clf()