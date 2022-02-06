from math import sin, sqrt

def un(u0, n) :
    r = u0
    for i in range (n) :
        r = sin(r)
    return r

u0 = float(input("u0 = "))
n = int(input("n = "))
u_n = un(u0, n)
print(u_n)
print(u_n/sqrt(3/n))