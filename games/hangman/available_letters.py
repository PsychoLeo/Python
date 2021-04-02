def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    l_alph = []
    
    for k in range (len(alph)) :
        l_alph.append (alph[k])
    
    for i in lettersGuessed :
        l_alph.remove(i)
    return ''.join(l_alph)