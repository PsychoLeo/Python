# difficult part

'''
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

fig = Figure ()
canvas = FigureCanvas (fig)

import numpy as np

x = np.random.randn (10000)

ax = fig.add_subplot (111) # creates a grid w. 1 row and 1 column
ax.hist (x, 100)

ax.set_title ('Normal distribution with $\mu=0, \sigma=1$')
# fig.savefig ('matplotlib_histogram.png')
'''

# easy part

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn (10000)
plt.hist (x, 100)
plt.title ('Normal distribution with $\mu=0, \sigma=1$')
plt.show ()