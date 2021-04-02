import random
from string import ascii_lowercase

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return set([i for i in secretWord]) <= (set (lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ''.join ([(i if i in lettersGuessed else '_ ') for i in secretWord])

    
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    return ''.join ([i for i in ascii_lowercase if i not in set(lettersGuessed)])


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print ('Welcome to the game, Hangman !')
    print ('I am thinking of a word that is %s letters long.' % (len(secretWord)))
    
    n_guesses = 8
    lettersGuessed = []
    l_secretWord = []
    
    for k in range (len(secretWord)) :
        l_secretWord.append (secretWord[k])
    
        
    while n_guesses != 0 and isWordGuessed(secretWord, lettersGuessed) == False :
        
        print ('-----------')
        print ('You have %s guesses left.' % (n_guesses))
        print ('Available letters : %s' % (getAvailableLetters (lettersGuessed)))
        letter = input ('Please guess a letter : ')
        letter = letter.lower ()
        
        
        if letter not in lettersGuessed :
            lettersGuessed.append (letter)
            if letter in secretWord :
                print ('Good guess : ', getGuessedWord(secretWord, lettersGuessed))

            else :
                print ('Oops ! That letter is not in my word : ', getGuessedWord(secretWord, lettersGuessed))
                n_guesses -= 1
                      
        else :
            print ('Oops ! You\'ve already guessed that letter : ', getGuessedWord(secretWord, lettersGuessed))   
            
    
    if isWordGuessed(secretWord, lettersGuessed) == True :
        print ('-----------')
        print ('Congratulations, you won !')
    
    else :
        print ('-----------')
        print ('Sorry, you ran out of guesses. The word was %s.' % (secretWord))

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
