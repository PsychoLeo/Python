# method n°1 : works but Pizzaz.garden_feast is ismpossible as Pizza
# types are subclasses of Pizzaz

class Pizzaz :
    
    orders = 1
    def __init__ (self, ingredients) :
        self.ingredients = ingredients
        self.order_number = Pizzaz.orders
        Pizzaz.orders += 1
        
class garden_feast (Pizzaz) :
    def __init__ (self) :
        Pizzaz.__init__ (self, [])
        self.ingredients = ['spinach', 'olives', 'mushroom']
        
class hawaiian (Pizzaz) :
    def __init__ (self) :
        Pizzaz.__init__ (self, [])
        self.ingredients = ['ham', 'pineapple']
    
class meat_festival (Pizzaz) :
    def __init__ (self) :
        Pizzaz.__init__ (self, [])
        self.ingredients = ['beef', 'meatball', 'bacon']
        
##########################################
# method n°2 : pizza types being functions of Pizza class

class Pizza :
    
    orders = 1
    
    def __init__ (self, ingredients) :
        self.ingredients = ingredients
        self.order_number = Pizzaz.orders
        Pizzaz.orders += 1
    
    @classmethod
    def hawaiian (self) :
        Pizza.__init__ (self, [])
        self.ingredients = ['ham', 'pineapple']
     
    @classmethod 
    def garden_feast (self) :
        Pizza.__init__ (self, [])
        self.ingredients = ['spinach', 'olives', 'mushroom']
     
    @classmethod 
    def meat_festival (self) :
        Pizza.__init__ (self, [])
        self.ingredients = ['beef', 'meatball', 'bacon']
        
#########################################
# program found in the solution section

class Pizza:
    
    orders = 0
    def __init__(self, ingredients):
        self.ingredients = list(ingredients)
        self.order_number = self.get_order_number()
        
    def get_order_number(self):
        Pizza.orders += 1
        return Pizza.orders
        
    def garden_feast():
        return Pizza(['spinach', 'olives', 'mushroom'])
        
    def hawaiian():
        return Pizza(['ham', 'pineapple'])
        
    def meat_festival():
        return Pizza(['beef', 'meatball', 'bacon'])