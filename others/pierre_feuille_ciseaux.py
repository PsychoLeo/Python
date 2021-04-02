import random
import sys

# init = int(input("Pierre feuille ciseaux ? Si oui, rentrez 1, sinon 0 : "))

def jeu() :
  
    jeu_ordi = random.randint (1, 3)
    jeu_joueur = int(input("Entrez ce que vous voulez jouer : 1 pour pierre, 2 pour feuille et 3 pour ciseaux : "))
    score_ordi = 0
    score_joueur = 0
    
    if jeu_joueur == 3 and jeu_ordi == 1 or jeu_joueur == 2 and jeu_ordi == 3 or jeu_joueur == 1 and jeu_ordi == 2 :
        print ("Perdu !")
        score_ordi += 1
    elif jeu_joueur == 1 and jeu_ordi == 3 or jeu_joueur == 3 and jeu_ordi == 2 or jeu_joueur == 2 and jeu_ordi == 1 :
        print ("Gagné !")
        score_joueur += 1
    elif jeu_joueur == jeu_ordi :
        print ("Egalité")
  
    ordi = "L'ordinateur a joué "
    if jeu_ordi == 1 :
        print (ordi, "pierre")
    elif jeu_ordi == 2 :
        print (ordi, "feuille")
    else :
        print (ordi, "ciseaux")

    print ("Ordinateur : %s -- %s : Vous" % (score_ordi, score_joueur))
    rejouer = input("Voulez-vous rejouer : entrer o si oui et n si non : ")
    if rejouer == 'o':
        jeu ()
    elif rejouer == 'n' :
        sys.exit ()

'''if init == 1 :
  jeu ()
else :
  print ("Je ne vois pas ce que vous faites ici alors.")'''
  
  
##############################################
# new version 2.0 - july 2020

score = [0, 0]
Quit = 0

# 0 -> rock
# 1 -> paper
# 2 -> scissors

def game () :
    
    global score, Quit
    
    while Quit == 0 :
        
        p = int (input ('Enter what you want to play : 0 for rock, 1 for paper and 2 for scissors : '))
        c = random.randint (0, 2)
        
        if c == 0 and p == 2 or c == 1 and p == 0 or c == 2 and p == 1:
            score [0] += 1
            print ('You lost ! Score : Computer %s - %s Player' % (score [0], score [1]))
            print ('')
            Quit = int (input ('Would you like to quit ? Enter 0 if not (other game), else 1 : '))
        elif p == 0 and c == 2 or p == 1 and c == 0 or p == 2 and c == 1:
            score [1] += 1
            print ('You won ! Score : Computer %s - %s Player' % (score [0], score [1]))
            print ('')
        elif c == p :
            print ('Both played the same !')
            print ('')
            return game ()
        else :
            print ('Invalid command')
            print ('')
            return game ()
    
    return None
    
if __name__ == '__main__' :
    choice = input("Rock paper scissors ? Press Enter to play or anything else to quit : ")
    print ('')
    if choice == '' :
        game ()