from pprint import pprint

def id_matrix (n) :
    assert isinstance (n, int) == True, "'n'must be an integer"
    if n >= 0 :
        return pprint ([[1 if i == j else 0 for i in range (n)] for j in range (n)])
    else :
        return pprint ([[1 if i == -n-j-1 else 0 for i in range (-n)] for j in range (-n)])
    
#############################################################

def id_mtrx (n) :
    if isinstance (n, int) == False :
        return 'Error'
    elif n >= 0 :
        return [[1 if i == j else 0 for i in range (n)] for j in range (n)]
    else :
        return [[1 if i == -n-j-1 else 0 for i in range (-n)] for j in range (-n)]