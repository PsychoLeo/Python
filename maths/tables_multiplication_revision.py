# revision des tables de multiplication

from random import randint

note = 0
minimum = 2
maximum = 20

print ('Bienvenue, nous allons vous faire revoir vos tables de multiplication !')
name = input ('Quel est votre prenom ? ')
print ('Bienvenue', name, '!')
n = int(input('Combien de calculs voulez-vous faire ? '))

for i in range (n) :
    j = randint (minimum, maximum)
    k = randint (minimum, maximum)
    result = int(input( 'Combien font %s fois %s ? ' % (j, k)))
    if result == j*k :
        print ('Bien joue !')
        print ('')
        note += 1
    else :
        print ('Mauvaise reponse ! La bonne reponse etait', j*k)
        print ('')

print ('Le test est termine, votre note est de %s / 20' % round(note*20/n, 2))
