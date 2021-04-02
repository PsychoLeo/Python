from math import cos, sin, pi

# delta = 0.001
# x = -pi
# up = -12
# while x <= pi :
#     if 1-delta < 3*sin(x) - cos(2*x) < 1+delta :
#         print (up)
#     x += pi/12
#     up += 1

# print (1+cos(6))
# print (1+cos(2))
# print (1+cos(4))
# print (1+cos(1))

def f(x) :
    return (-4*x-3)/(2*x+sin(4*x))

print (f(-1000000))