# pdf sur les jeux python

from random import randint, sample, choice, shuffle
from pprint import pprint

# simulation d'un lancer de dé pipé
def de_pipe_lancer (n) :
    vals = []
    for i in range (n) :
        r = randint (1, 20)
        if r <= 2 :
            vals.append (1)
        elif r <= 8 and r > 2 :
            vals.append (6)
        else :
            vals.append (choice([2, 3, 4, 5]))
    return vals


def choice (l) :
    return l[randint (0, len(l)-1)]
# equivalent of random choice function


# tire un paquet de cartes hearthstone :
# 5 cartes, rareté commune, rare, épique, légendaire
def tirage_hearthstone () :
    l = []
    for i in range (5) :
        r = randint (1, 100)
        if r <= 1 :
            l.append ('L')
        elif 1 < r <= 5 :
            l.append ('E')
        elif 5 < r <= 28 :
            l.append ('R')
        else :
            l.append ('C')
    if 'R' not in l :
        return tirage_hearthstone ()
    else :
        return print (' '.join (l))
    
def tirage_de () :
    r = randint (1, 4)
    if r == 1 :
        return r, randint (1, 6)
    elif r == 2 :
        return r, randint (1, 8)
    elif r == 3 :
        return r, randint (1, 10)
    else :
        return r, randint (1, 12)
    

def risk (offense, defense) :
    de = [1, 2, 3, 4, 5, 6]
    return max([choice(de) for _ in range (offense)]) > max([choice(de) for _ in range (defense)])

def celsius_fahrenheit (t, mode) :
    if mode == 'cf' :
        return round((9/5)*t+32, 2)
    elif mode == 'fc' :
        return round((5/9)*(t-32), 2)
    else :
        return 'Invalid input'
    
def f(mini, maxi, pas) :
    l = []
    while mini < maxi :
        l.append (mini)
        mini += pas
    return [(i, 2*i**3-3*i-1) for i in l]
        

# jour de la semaine avec année, jour, mois (depuis l'an 1583)
def weekday (d, m, y) :
    day = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}
    if m < 3 :
        z = y - 1
    else :
        z = y
    k = (23*m)//9 + d + 4 + y + z//4 - z//100 + z//400
    if m < 3 :
        return day[k % 7]
    else :
        return day[(k-2) % 7]
    
# échange valeur et clés dans un dictionnaire
def change_key_value (dic) :
    pprint ({list(dic.values())[i] : list(dic.keys())[i] for i in range (0, len(dic))})
    return None

# play game anagrame

def anagram () :
    words = ''.join([i.rstrip ('\n') for i in open ('/home/leo/Bureau/Programmation/Python/programs/mots.txt', 'r')])
    lwords = words.split (' ')
    correct = list (choice (lwords))
    cst_correct = correct.copy()
    while True :
        shuffle (correct)
        print (''.join (correct))
        ask = input ('Enter the word you think it is : ')
        if ask == ''.join(cst_correct).lower () :
            return 'Well played !'
        else :
            print ('Bad guess, try again !')
            
# suivant
    
    