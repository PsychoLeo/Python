from random import *
from time import sleep


#######################################################################

class Player :
    
    def __init__ (self, trophies, coins, fighters) :
        self.trophies = trophies
        self.coins = coins
        self.fighters = fighters
        
    def ser_trophies (self, trophies) :
        self.trophies += trophies
        return None
    
    def set_fighters (self, fighter) :
        self.fighters.append (fighter)
        return None
    
    def set_coins (self, coins) :
        self.coins += coins
        return None
    
    get_trophies = lambda self : self.trophies
    get_coins = lambda self : self.coins
    get_fighters = lambda self : self.fighters
    

#######################################################################

class Chest :
    
    def __init__ (self, rarity) :
        self.rarity = rarity
        
    def open_chest (self) :
        pass
    
    get_rarity = lambda self : self.rarity
    
    def set_rarity (self, rarity) :
        self.rarity = rarity
    

#######################################################################

class Fighter :
    
    # initializing variables and attributes of fighters
    def __init__ (self, health, attack, attack_speed, capacity, capacity_speed, capacity_reload = 0, shield = 0) :
        self.stored = [health, attack, attack_speed, capacity, capacity_speed, capacity_reload, shield]
        self.health = health
        self.attack = attack
        self.attack_speed = attack_speed
        self.capacity = capacity
        self.capacity_speed = capacity_speed
        self.capacity_reload = capacity_reload
        self.shield = shield
    
    # simulate one attack
    def do_attack (self, other) :
        other.health -= self.attack*self.attack_speed/10
    
    # simulate fight between 2 entities
    def fight (self, other) :
        
        while self.health > 0 and other.health > 0 :
            print (self.health, other.health)
            Fighter.do_attack (self, other)
            Fighter.do_attack (other, self)
            self.capacity_reload += 1
            other.capacity_reload += 1
            if self.capacity_reload == self.capacity_speed :
                self.use_capacity (other)
            if other.capacity_reload == other.capacity_speed :
                other.use_capacity (self)
        
        if self.health <= 0 and other.health <= 0 :
            self.health = self.stored[0] # how to reset a value in a class after being modified
            other.health = other.stored[0]
            self.set_capacity_reload (0)
            return 'Draw'
        elif self.health > 0 : # no need to include other.health <= 0
            self.health = self.stored[0]
            other.health = other.stored[0]
            self.set_capacity_reload (0)
            return '1 won' # search on how to call an instance by its initialization name
        else :
            self.health = self.stored[0]
            other.health = other.stored[0]
            self.set_capacity_reload (0)
            return '2 won'
            
    
    # using a Fighter's capacity
    def use_capacity (self, other) :
        if self.capacity == 'shield' :
            self.set_shield (0.5) # percentage of shield reduction (50% here)
        elif self.capacity == 'rage' :
            self.set_attack (1.4*self.attack) # longer period than last_bullet (try change that) --> how to measure time ?
        elif self.capacity == 'last_bullet' :
            self.set_attack (2*self.attack)
        elif self.capacity == 'freeze' :
            pass
        self.set_capacity_reload (0)
        
    
    
    # defining getters
    get_stored = lambda self : self.stored
    get_health = lambda self : round(self.health)
    get_attack = lambda self : round(self.attack)
    get_attack_speed = lambda self : round(self.attack_speed)
    get_capacity = lambda self : round(self.capacity)
    get_capacity_speed = lambda self : round(self.capacity_speed)
    get_shield = lambda self : round(self.shield)
    
    # defining setters
    
    def set_health (self, health) :
        self.health = health
        return None
    
    def set_attack (self, attack) :
        self.attack = attack
        return None
    
    def set_attack_damage (self, attack_damage) :
        self.attack_damage = attack_damage
        return None
    
    def set_capacity (self, capacity) :
        self.capacity = capacity
        return None
    
    def set_capacity_speed (self, capacity_speed) :
        self.capacity_speed = capacity_speed
        return None
    
    def set_shield (self, shield) :
        self.shield = shield
        return None
    
    def set_capacity_reload (self, capacity_reload) :
        self.capacity_reload = capacity_reload
        return None
    
#######################################################################

class Sniper (Fighter) :
    
    def __init__ (self, lvl) :
        Fighter.__init__ (self, round(1300*1.06**lvl), round(1200*1.06**lvl), 6, 'last_bullet', 4)
        self.lvl = lvl
        
    get_lvl = lambda self : self.lvl
    
    def set_lvl (self, lvl) :
        self.lvl = lvl
        return None

#############################

class Gladiator (Fighter) :
    
    def __init__ (self, lvl) :
        Fighter.__init__ (self, round(2400*1.06**lvl), round(700*1.06**lvl), 9, 'shield', 5)
        self.lvl = lvl
        
    get_lvl = lambda self : self.lvl
    
    def set_lvl (self, lvl) :
        self.lvl = lvl
        return None
    
#############################
    
class Troll (Fighter) :
    
    def __init__ (self, lvl) :
        Fighter.__init__ (self, round(3200*1.06**lvl), round(1100*1.06**lvl), 4, 'rage', 6)
        
    get_lvl = lambda self : self.lvl
    
    def set_lvl (self, lvl) :
        self.lvl = lvl
        return None
    
#############################