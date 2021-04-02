from string import ascii_lowercase

alph = list(ascii_lowercase)
banned = []
CRACK_LENGTH = 20 # minimal size of message to be cracked using letter occurences

# encrypt and decrypt function
def caesar_cipher (mode, msg, key) :
    '''
    input : mode (encrypt, decrypt), message to encrypt or decrypt and key used for it
    output : encrypted / decrypted message
    '''
    l_msg = [alph.index(i) if i in alph else i for i in msg]
    if mode == 'encrypt' :
        return ''.join([alph[(i+key)%26] if type(i) == int else i for i in l_msg])
    else :
        return ''.join([alph[(i-key)%26] if type(i) == int else i for i in l_msg])
    
# crack function    
def crack (msg) :
    '''
    input : the message to decrypt (without knowing the key)
    output : the decrypted message and the key associated with it
    '''
    l_msg = [alph.index(i) if i in alph else i for i in msg]
    if len (msg) < CRACK_LENGTH :
        return crack_brute (msg)
    else :
        return crack_occur (msg)


# cracking with brute force method function
def crack_brute (msg) :
    '''
    input : the message to decrypt using brute force
    output : the decrypted message and the key associated with it
    '''
    l_msg = [alph.index(i) if i in alph else i for i in msg]
    for j in range (1, 26) :
        print (''.join([alph[(i-j)%26] if type(i) == int else i for i in l_msg]))
        n = input ("Is the message correct ? Enter 'o' if yes and  press enter if not : ")
        print ('')
        if n == 'o' :
            key = j
            break
    return ('The key was %s' % key)


# cracking with letter occurences method function
def crack_occur (msg) :
    '''
    input : the message to decrypt using letter occurences
    output : the decrypted message and the key associated with it
    '''
    l_msg = [alph.index(i) if i in alph else i for i in msg]
    msg_list = [i for i in msg if i not in banned]
    maximum_occur = max([i for i in msg_list if i in alph], key = [i for i in msg_list if i in alph].count)
    diff = (alph.index (maximum_occur) - alph.index ('e')) % 26
    print (''.join([alph[(i - diff)%26] if type(i) == int else i for i in l_msg]))
    n = input ("Is the message correct ? Enter 'o' if yes and  press enter if not : ")
    print ('')
    if n == 'o' :
        key = diff
        return ('The key was %s' % key)
    else :
        banned.append (maximum_occur)
        return crack_occur (msg)


# running the program by itself
if __name__ == '__main__' :
    mode = input('Enter the mode you want to use (encrypt / decrypt / crack) : ')
    msg = input('Enter the message you want to %s : ' % mode).lower ()
    if mode == 'encrypt' or mode == 'decrypt' :
        key = int(input('Enter the key you want to use to %s the message : ' % mode))
        print (caesar_cipher (mode, msg, key))
    else :
        print (crack (msg))