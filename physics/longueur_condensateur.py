from math import sqrt

t1 = 7.96*10**(-7)
q = 1.602*10**(-19)
U = 24
m = 1.67*10**(-27)

for n in range (2, 6) :
    print (t1*sqrt(q*U/(2*m))*(1/(sqrt(n)-sqrt(n-1)))*100)