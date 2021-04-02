# import numpy as np
import time
import pycld2 as cld2 # analyzing if words are in a particular language or not

class Vigenere :

    alph_string = 'abcdefghijklmnopqrstuvwxyz' # string alphabet for indexing
    alph_set = set('abcdefghijklmnopqrstuvwxyz') # set alphabet for finding if elements are in it

    def __init__ (self, message, mode, key=None) : # all texts are converted to lowercase
        self.message = message.lower()
        self.mode = mode
        self.len_msg = len(self.message)
        self.key_map = {letter:Vigenere.alph_string.index(letter) for letter in Vigenere.alph_set}
        if key != None : # if key was given (not crack mode)
            self.key = key.lower()
            self.len_key = len(self.key)
    
    def translate (self) : # decrypt or encrypt
        '''
        Input : class attributes (mode)
        output : decrpyted / encrypted message using key
        '''
        assert self.mode in {'d', 'e', 'c'}, "Mode has to be 'd', 'e' or 'c'"
        if self.mode == 'd' :
            return self.decrypt(self.key)
        else : # if mode is encrypt 
            return self.encrypt()

    def encrypt (self) :
        '''
        input : class attributes (message, key, ...)
        output : decrypted message using the key
        '''
        assert self.key != None, 'Encryption key was not defined'
        result, j = '', 0 # variable résultat et variable du nombre de lettres possiblement changeables
        for i in range(self.len_msg) :
            # print (self.message[i])
            if self.message[i] not in Vigenere.alph_string : # if character is not a letter
                result += self.message[i]
            else : # if character is a letter
                translated_index = self.key_map[self.message[i]]
                key_index = self.key_map[self.key[j%self.len_key]]
                index = (translated_index+key_index)%26 # index de la bonne lettre
                result += Vigenere.alph_string[index]; j += 1
        return result

    
    def decrypt(self) :
        '''
        input : class attributes (message, key,...)
        output : decrypted message using the key
        '''
        assert self.key != None, 'Decryption key was not defined'
        result, j = '', 0 # variable résultat et variable du nombre de lettres possiblement changeables
        for i in range(self.len_msg) :
            # print (self.message[i])
            if self.message[i] not in Vigenere.alph_string : # if character is not a letter
                result += self.message[i]
            else : # if character is a letter
                translated_index = self.key_map[self.message[i]]
                key_index = self.key_map[self.key[j%self.len_key]]
                index = (translated_index-key_index)%26 # index de la bonne lettre
                result += Vigenere.alph_string[index]; j += 1
        return result



class frequencyAnalysis (Vigenere) :

    def __init__ (self, message, mode) : # same as Vigenere except we don't modify self.message
        Vigenere.__init__(self, message, mode)

    def crack (self, num_keys=50) :
        '''
        input : None
        output : None, printing out questions to find out if key is correct
        '''
        keys, foundReliable = [], False
        for i in range (1, num_keys+1) :
            r = self.findKey(i)
            keys.append(r)
            decrypted_text = self.decryptText(self.message, r)
            isReliable, textBytesFound, details = cld2.detect(decrypted_text)
            if isReliable :
                print (f'Key : {r}')
                print (f'Decrpyted message :')
                foundReliable = True
                break # considering this is the message
        return decrypted_text if foundReliable else 'No key found'
        

    def decryptText(self, msg, key) :
        '''
        input : class attributes (message, key,...)
        output : decrypted message using the key
        '''
        key_map = {letter:Vigenere.alph_string.index(letter) for letter in Vigenere.alph_set}
        assert key != None, 'Decryption key was not defined'
        result, j = '', 0 # variable résultat et variable du nombre de lettres possiblement changeables
        for i in range(len(msg)) :
            if msg[i] not in Vigenere.alph_set : # if character is not a letter
                result += msg[i]
            else : # if character is a letter
                translated_index = key_map[msg[i]]
                key_index = key_map[key[j%len(key)]]
                index = (translated_index-key_index)%26 # index de la bonne lettre
                result += Vigenere.alph_string[index]; j += 1
        return result


    def findKey (self, key_len) :
        '''
        input : message (string) and a key length (int)
        output : the most likely key 
        Only works for long messages
        '''
        possible_key, i = '', 0
        while i < key_len : # while we have not made up a full word
            text = self.getText(i, key_len) # text to translate with the key
            match_scores = {char:0 for char in Vigenere.alph_set} # match scores of letters
            for letter in Vigenere.alph_set : # try every letter as key
                current_message = self.decryptText(text, letter) # decrypt text with the current letter as key
                occurences = self.getFrequency(current_message) # dictionnary of all letters and their frequencies
                sorted_scores = sorted(list(occurences.keys()), key=occurences.get)
                letter_score = self.letterScore(letter, sorted_scores) # returns the score of the given letter
                match_scores[letter] = letter_score # changing the letter score to its value 
            possible_key += max(match_scores, key=match_scores.get)
            i += 1
        return possible_key
    

    def letterScore (self, letter, sorted_scores) :
        '''
        input : letter and list of letters from less to most frequent using this letter as key
        output : the score performed by the letter in frequency of recurring english letters
        '''
        score = 0
        for score_letter in sorted_scores[:6] : # if not common letters do not appear when using this letter as key
            if score_letter in 'vkjxqz' :
                score += 1
        for score_letter in sorted_scores[-6:] : # if common letters appear when using this letter as key
            if score_letter in 'etaoin' :
                score += 1
        return score

    
    def getFrequency (self, msg) :
        '''
        input : message in lowercase (string)
        output : the number of occurences of each letter (dictionnary)
        '''
        occurences = {letter:0 for letter in Vigenere.alph_set} # occurences of each letter
        for i in msg :
            if i in Vigenere.alph_set :
                occurences[i] += 1 # increment each letter occcurence
        return occurences


    def getText(self, start_index, key_len) :
        '''
        input : class attributes, start index and key length
        output : returning tet every n indexes (without spaces and special characters)
        '''
        text = [char for char in self.message if char in Vigenere.alph_set]
        return ''.join([text[i] for i in range(start_index, len(text), key_len)])


pathB = '/home/leo/Bureau/Programmation/Python/cryptography/vigenere/vigenere_cipher_history.txt'
with open(pathB, 'r') as f :
    uncrypted_txt = f.read()

pathA = '/home/leo/Bureau/Programmation/Python/cryptography/vigenere/vigenere_cipher_history_crypted.txt'
with open(pathA, 'r') as f :
    crypted_txt = f.read()
# key is kibitragne

mode = input('Enter the mode [d/e/c] (decrypt/encrypt/crack) : ')

if __name__ == '__main__' :
    if mode == 'c' :
        message = crypted_txt
        start = time.time()
        cipher = frequencyAnalysis(message, mode)
        print(cipher.crack())
    else :
        key = 'jedosqsopaapospolkjkdjfaz'
        if mode == 'd' : 
            message = crypted_txt
        else :
            message = uncrypted_txt
        assert all([letter in Vigenere.alph_string for letter in key.lower()]), 'Key has non-letter characters'
        start = time.time()
        cipher = Vigenere(message, mode, key)
        print(cipher.translate())
    print(f'Time : {time.time()-start} seconds')