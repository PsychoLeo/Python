from random import choice

def juniper_green (nmax) :
    
    banned = []
    possible = [i for i in range (1, nmax+1)]
    plays = 0
    
    while possible != [] :
        
        print ('Valid numbers : ' + str(possible))
        play = int(input ('Enter your play : '))
        
        
        if play in possible and play not in banned :
            
            if plays == 0 and play % 2 != 0 :
                return 'You lost ! First number played has to be even !'
            
            # human play consideration
            possible = [i for i in range (1, play) if play % i == 0]
            possible += [play*i for i in range (1, nmax//play+1) if play*i <= nmax]
            banned.append (play)
            possible = [i for i in possible if i not in banned]
            plays += 1
            
            # computer play consideration
            try :
                comp_play = choice (possible)
                banned.append (comp_play)
                possible = [i for i in range (1, comp_play) if comp_play % i == 0]
                possible += [comp_play*i for i in range (1, nmax//comp_play+1) if comp_play*i <= nmax]
                possible = [i for i in possible if i not in banned]
                print ('Computer plays %s' % comp_play)
        
            except IndexError :
                return 'You won ! Computer is not able to play !'
            
        else :
            return 'You lost ! You played a number twice !'
        
        