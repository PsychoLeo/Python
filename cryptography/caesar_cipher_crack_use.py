from string import ascii_lowercase
# import pyperclip --> si je veux ajouter des fonctions copier / coller


def caesar_cipher (mode, msg, key) :
    
    '''input : mode (encrypt, decrypt), message and key used for it
    output : encrypted / decrypted message'''
    
    alph = list(ascii_lowercase)
    l_msg = [alph.index(i) if i in alph else i for i in msg]
    
    if mode == 'encrypt' :
        return ''.join([alph[(i+key)%26] if type(i) == int else i for i in l_msg])
    
    elif mode == 'decrypt' :
        return ''.join([alph[(i-key)%26] if type(i) == int else i for i in l_msg])
    
    else :
        return ('Please enter a valid mode')
    

def crack_caesar_cipher (msg) :
    
    alph = list(ascii_lowercase)
    l_msg = [alph.index(i) if i in alph else i for i in msg]
    
    if len(msg) < 100 : # method 1 : brute forcing the code
        for j in range (1, 26) :
            print (''.join([alph[(i-j)%26] if type(i) == int else i for i in l_msg]))
            n = input ("Is the message correct ? Enter 'o' if yes and  press enter if not : ")
            print ('')
            
            if n == 'o' :
                key = j
                break
        
        return ('The key was %s' % key)

    else :
        
        msg_list = [i for i in msg]
        maximum_occur = max([i for i in [i for i in msg] if i in alph], key = [i for i in [i for i in msg] if i in alph].count)
        diff = alph.index (maximum_occur) - alph.index ('e')
        print (''.join([alph[(i - diff)%26] if type(i) == int else i for i in l_msg]))
        n = input ("Is the message correct ? Enter 'o' if yes and  press enter if not : ")
        print ('')
        
        if n == 'o' :
            key = diff
        else :
            pass
        return ('The key was %s' % key)
    

if __name__ == '__main__' :
    
    mode = input('Enter the mode you want to use (encrypt / decrypt / crack) : ')
    msg = input('Enter the message you want to %s : ' % mode)
    
    if mode == 'encrypt' or mode == 'decrypt' :
        key = int(input('Enter the key you want to use to %s : ' % mode))
        print (caesar_cipher (mode, msg, key))
    else :
        print (crack_caesar_cipher (msg))
        
        
def caesar (txt, key) :
    txt = list(txt.lower ())
    for i in range (len(txt)) :
        if txt[i] in alph :
            txt[i] = alph [(alph.index(txt[i])+key)%26]
    return ''.join(txt)