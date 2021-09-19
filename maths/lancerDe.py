import random

def runExp(nbLancers = int(1e6), n=int(1e3)):
    sumApparitions = 0
    for lancer in range(nbLancers):
        tour = 1
        while random.randint(1,6) != 6 and tour <= n:
            tour+=1
        if tour <= n:
            sumApparitions += tour
        
    return sumApparitions/nbLancers

if "__main__" == __name__:
    print(runExp())
