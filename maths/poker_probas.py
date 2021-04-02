card = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}

n = 47 # nombre de cartes restantes dans le deck à distribuer (52 - nombre de cartes en main / milieu)

def p_paire (jeu) :
    paire = 3/n + 3/(n-1) + (3/n)*(2/(n-1)) # proba paire ou plus en deux coups, si le joueur n'a rien dans son jeu (proba paire 1e carte, proba paire 2e carte, proba paire 1e carte et 2e carte --> brelan)
    for i in range (len(jeu)) :
        for j in range (len(jeu)) :
            if i != j :
                if jeu[i] == jeu[j] :
                    paire = 1 # proba paire si le joueur a une paire
                    break
    return round (paire*100, 2)

def p_brelan (jeu) :
    brelan = (3/n)*(2/(n-1)) # si joueur n'a aucune paire, il doit avoir la bonne carte 2 fois d'affilée, donc proba brelan est proba 1e carte * proba 2e carte 
    for i in range (len(jeu)) :
        for j in range (len(jeu)) :
            if i != j:
                if jeu[i] == jeu[j] :
                    brelan = 2/n + 2/(n-1) + (2/n)*(1/(n-1)) # proba brelan si le joueur a une paire, il peut donc avoir la bonne carte au 1e tour, au deuxième, ou aux deux --> carré
                    for k in range (len(jeu)) :
                        if k != j and k != i :
                            if jeu[k] == jeu[i] :
                                brelan = 1 # proba brelan si le joueur a un brelan dans son jeu
                                break
    return round (brelan*100, 2)

def p_double_paire (jeu) :
    double_paire = (15/n)*(12/(n-1)) # proba double paire si le joueur n'a aucune paire en main (5*3)/n + (4*3)/n
    '''if p_paire (jeu) == 1 :''' # technique potentiellement utilisable (mais pas facile et pas sûr du résultat
    for i in range (len(jeu)) :
        for j in range (len(jeu)) :
            
        
                

if __name__ == '__main__' :
    
    jeu = []
    
    for i in range (5) :
        jeu_carte = input('Entrer la carte du jeu n°%s : ' % (i+1))
        jeu.append (jeu_carte)
    
    print ('')
    
    print ('paire : ', p_paire (jeu))
    print ('double paire : ', p_double_paire (jeu))
    print ('brelan : ', p_brelan (jeu))
    '''
    p_suite (jeu)
    p_couleur (jeu)
    p_full (jeu)
    p_carre (jeu)
    p_quinte_flush (jeu)
    p_quinte_flush_royale (jeu)'''