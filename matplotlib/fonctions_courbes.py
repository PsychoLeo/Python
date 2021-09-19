# import matplotlib.pyplot as plt
# from math import *
# x = [ i for i in range (-10,11)]
# y = [(j**2-5) for j in x]
# plt.plot(x,y)
# plt.grid()
# plt.plot(x,y,marker='+')
# plt.show()

for i in range (10, 100) :
    if 10 <= int(str(i)[::-1]) < i and ((i-int(str(i)[::-1]))**(1/3)).is_integer() :
        print(i, int(str(i)[::-1]))