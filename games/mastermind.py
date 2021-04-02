import random
from collections import Counter
from pprint import pprint

class Mastermind :
    
    # for the moment, the game is only against computer / initializing variables
    def __init__ (self, ncolors = 6, lrows = 4, maxplays = 12) :
        self.ncolors = ncolors
        self.lrows = lrows
        self.maxplays = maxplays
        self.combination = ''.join([str(random.randint (1, self.ncolors)) for _ in range (self.lrows)])
        self.game = [[] for _ in range (self.maxplays)]
        self.plays = 0
    
    # getting the user's input of a combination
    def ask (self, guess) :
                
        '''input : two strings of guess about what is the secret combination
        output : the number of elements in common (one element only matches another)'''
        
        guess = str(guess)
        assert len(guess) == len(self.combination), 'User\'s guess and hidden self.combination must have same length'
        
        if guess == self.combination :
            return 'You won ! Initialize another game to keep playing !'
        
        if self.plays >= self.maxplays :
            return 'Game Over ! Initialize another game to keep playing!'
        
        blacks = []
        
        for i in range (len(self.combination)) :
            if guess[i] == self.combination[i] :
                blacks += self.combination [i]
        
        whites = list((Counter(guess) & Counter(self.combination)).elements())
        
        for i in blacks :
            if i in whites :
                whites.remove (i)
        
        for k in range (len(self.combination)) :
            self.game[self.plays] += ' ' + guess[k] + '  '
        self.game[self.plays] += ' ||   Blacks: %s  -  Whites: %s  ' % (len(blacks), len(whites))
        self.game[self.plays] = ''.join(self.game[self.plays])
        
        pprint (self.game)
        self.plays += 1
        return None
    
    
    # asking for the number of plays remaining
    def get_plays_left (self) :
        return self.maxplays - self.plays
    
    # resetting a game when done
    def reset (self) :
        self.__init__ (self.ncolors, self.lrows, self.maxplays)