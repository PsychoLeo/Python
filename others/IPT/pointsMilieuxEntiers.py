import random

def existeMilieuAvecCoordEntieres (l) :
    # O(n^2) -> faire avec pas trop de points
    n = len(l)
    for i in range (n) :
        for j in range (n) :
            if i != j : # si les 2 points ne sont pas les mêmes
                midX = (l[j][0] + l[i][0])%2==0
                midY = (l[j][1] + l[i][1])%2==0
                midZ = (l[j][2] + l[i][2])%2==0
                if midX and midY and midZ :
                    return True
    return False

def randomPt(maxi) :
    # on génère un tuple (x, y, z) de coords
    return (random.randint(0, maxi), random.randint(0, maxi), random.randint(0, maxi))


def generatePoints (n, maxi) :
    r = []
    for _ in range (n) :
        t = randomPt(maxi)
        r.append(t)
    return r

def main() :
    pointsGeneres = 5
    essais = 1000
    maxi = 100
    while True :
        potentialFound = True
        for i in range (essais) :
            listPoints = generatePoints(pointsGeneres, maxi)
            if not existeMilieuAvecCoordEntieres(listPoints) :
                potentialFound = False
                break
        if potentialFound :
            break
        pointsGeneres += 1
    print(pointsGeneres)

main()