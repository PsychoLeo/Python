from pprint import pprint

def diagonal_star (n) :
    
    '''input : the number of rows to make a star
    output : the printed star'''
    
    assert n >= 5, 'impossible to make a star with less than 5 rows'
    
    star = [['X' if x == 0 or x == n-1 else ' ' for x in range (n)] for y in range (n)]
    
    for i in range (n) :
        star[i][i] = 'X'
        star[n-i-1][i] = 'X'
    
    '''for i in range (len(star)) :
        if star[i] == 0 or star[i] == n-1 :
            for j in range (len(star[i])) :
                star[i][j] = 'X' '''
    
    return pprint (star)