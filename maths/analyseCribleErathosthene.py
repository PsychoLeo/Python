import matplotlib.pyplot as plt
from math import log

def crible (n) :
    nbOper = 0
    prime = [True]*n
    prime[0] = prime[1] = False
    for i in range (2, n) :
        if prime[i] :
            nbOper += 1
            for j in range (2*i, n, i) :
                nbOper += 1
                prime[j] = False
    return nbOper

if __name__ == '__main__': 
    plt.style.use("seaborn")
    # plt.xscale("log")
    # plt.yscale("log")
    plt.title("Analyse asymptotique du crible d'Ératosthène")
    plt.xlabel("Taille du crible (n)")
    plt.ylabel("Nombre d'itérations")
    nList = [10, 50, 100, 500, 10**3, 5000, 10**4, 5*10**4, 10**5, 5*10**5, 10**6, 5*10**6]
    iterationsCount = []
    asymptoticApproximation = [k*log(log(k)) for k in nList]
    for n in nList :
        # Compare n*ln(ln(n)) and crible number of operations
        iterationsCount.append(crible(n))
    plt.plot(nList, iterationsCount, label="Nombre d'itérations du crible")
    plt.plot(nList, asymptoticApproximation, color='r', label="Approximation n*ln(ln(n))")
    plt.legend()
    plt.show()