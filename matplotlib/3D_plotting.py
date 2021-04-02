import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import numpy as np
import random

#### Random points plotting ####
# fig1 = plt.figure ()
# ax1 = fig1.add_subplot (111, projection = '3d')
#
# x1 = list(range(10))
# y1 = [random.randint(0, i) for i in x1]
# z1 = [int(random.random()*10) for _ in range (10)]
#
# ax1.scatter (x1, y1, z1)
# plt.show ()


#### Spiral using cos and sin ####
# fig2 = plt.figure ()
# ax2 = fig2.add_subplot (111, projection = '3d')
#
# theta = np.linspace (-12, 12, 150)
# x2 = np.sin (theta)
# y2 = np.cos (theta)
# z2 = np.linspace (-2, 2, 150)
#
# ax2.plot (x2, y2, z2)
# plt.show ()


#### 3D normal distribution ####
random.seed (1)
x3 = [random.normalvariate(1, 1) for _ in range (400)]
y3 = [random.normalvariate(1, 1) for _ in range (400)]
z3 = [random.normalvariate(1, 1) for _ in range (400)]

fig3 = plt.figure ()
ax3 = fig3.add_subplot (111, projection = '3d')

ax3.scatter (x3, y3, z3)
ax3.set (xlabel='x axis', ylabel='y axis', zlabel='z axis')
plt.show ()
