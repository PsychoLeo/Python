from math import sqrt
import matplotlib.pyplot as plt

def main() :
    n = int(input("Entrer le nombre de points à représenter : "))
    z = complex(0.75, sqrt(3)/4)
    z_n = [1]
    for i in range (n) :
        z_n.append(z_n[-1]*z)
    plotPoints(z_n)

def plotPoints (values) :
    plt.style.use("seaborn")
    z1 = values[0]
    plt.scatter(z1.real, z1.imag, color='r')
    for z2 in values [1:] :
        plt.scatter(z2.real, z2.imag, color='r')
        plt.plot([z1.real, z2.real], [z1.imag, z2.imag], color = 'r')
        z1 = z2
    plt.title("Evolution de la suite z_n")
    plt.ylabel("Partie imaginaire de z_n")
    plt.xlabel("Partie réelle de z_n")
    plt.show()

main()