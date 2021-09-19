import matplotlib.pyplot as plt
from math import sin, pi

# f = lambda x: 2*x+3*sin(x)
def f(x) :
    return 2*x+3*sin(x)

x = [k*4*pi/2000 for k in range (2000)]
y = [f(i) for i in x]
plt.style.use('seaborn')
plt.plot(x, y)
plt.show()