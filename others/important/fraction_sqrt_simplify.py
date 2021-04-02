# fraction simplifier

from prime_factors import prime_facs

def simplify_fraction (txt) :
    
    '''input : a fraction (string form)
    output : this fraction, simplified '''
    
    assert isinstance (txt, str) == True
    
    fraction = [int(txt.split ('/')[0]), int(txt.split ('/')[1])]
    primefac = prime_facs (fraction[0])
    
    for i in primefac :
        while fraction[1] % i == 0 and fraction[0] % i == 0 :
            fraction[1] = fraction[1] / i
            fraction[0] = fraction[0] / i
    
    if (int(fraction[0]) / int(fraction[1])).is_integer () :
        return str(int(int(fraction[0]) / int(fraction[1])))
    else :
        return str(int(fraction[0])) + '/' + str(int(fraction[1]))
    
def simplify_sqrt(n):
    
    '''input : a number
    output : a tuple containing the number outside the sqrt and inside, after simplifying it '''
    
    simp = {i : prime_facs(n).count(i) for i in prime_facs (n)}
    ext = []
    for i in simp :
        if simp[i] >= 2 :
            for _ in range (simp[i] // 2) :
                ext.append (i)
                simp [i] -= 2
    simp = [i for i in simp if simp[i] == 1]
    return (multiply(ext), multiply(simp))

