import matplotlib.pyplot as plt
from math import *
x = [ i for i in range (-10,11)]
y = [(j**2-5) for j in x]
plt.plot(x,y)
plt.grid()
plt.plot(x,y,marker='+')
plt.show()