from math import sqrt
import gmpy

def function (a, b, c) :
    delta = b**2-4*a*c
    if delta < 0 :
        print ("L'équation n'a pas de solution dans R")
    elif delta == 0 :
        x0 = -b/2*a     
        print ("L'équation a une seule solution : x = %s" % (round(x0 ,3)))
    else :
        if gmpy.is_square(delta) == 1:
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)
            print ("L'équation a deux solutions : x = %s ou x = %s" % (round(x1, 3), round (x2, 3)))
        else :
            print ('''L'équation a deux solutions :
x = %s - sqrt(%s)/ %s ou x = %s + sqrt(%s)/ %s '''% (-b, delta, 2*a, -b, delta, 2*a))


if __name__ == '__main__' :
    a = float(input("Entrer a : "))
    b = float(input("Entrer b : "))
    c = float(input("Entrer c : "))
    function (a, b, c)