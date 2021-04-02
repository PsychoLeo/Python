import matplotlib.pyplot as plt
x = [ n for n in range (-10,11)]
y = [ (2*k-11)/(5*k+1) for k in x ]
plt.plot (x, y)
plt.grid ()
plt.show()