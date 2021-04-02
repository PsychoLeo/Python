class fraction (object) :
    
    def __init__ (self, numer, denom) :
        self.numer = numer
        self.denom = denom
        
    def __str__ (self) :
        return str (self.numer) + ' / ' + str (self.denom)
    
    def __add__ (self, other) :
        return self.numer / self.denom + other.numer / other.denom
    
    def __sub__ (self, other) :
        return self.numer / self.denom - other.numer / other.denom
    
    def __repr__ (self) :
        return 'fraction (' + str (self.numer) + ',' + str (self.denom) + ')'
    
    def Float (self) :
        return round (self.numer / self.denom, 3)
    
'''class ones_threes_nines:
    
    def __init__ (self, n) :
        
        self.nines = n // 9
        self.threes = n % 9 // 3
        self.ones = n % 9 % 3 // 1
        self.answer = "nines:"+ str(self.nines)+", threes:"+str(self.threes)+", ones:"+str(self.ones)'''