# import pyperclip

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main (mode, message, key) :
    if mode == 'encrypt' :
        translated = encryptMessage (key, message)
    else :
        translated = decryptMessage (key, message)

    print ('%sed message : ' % (mode))
    print (translated)
    # pyperclip.copy (translated)
    # print ()
    # print ('The message has been copied to the clipboard ')


def encryptMessage (key, message) :
    return translateMessage (key, message, 'encrypt')

def decryptMessage (key, message) :
    return translateMessage (key, message,'decrypt')

def translateMessage (key, message, mode) :
    translated = []

    keyIndex = 0
    key = key.upper ()
    
    for symbol in message :
        num = letters.find (symbol.upper ())
        if num != -1 :
            if mode == 'encrypt' :
                num += letters.find (key[keyIndex])
            elif mode == 'decrypt' :
                num -= letters.find (key[keyIndex])
            
            num %= len(letters)
            
            if symbol.isupper () :
                translated.append (letters [num])
            elif symbol.islower () :
                translated.append (letters[num].lower())
            
            keyIndex += 1
            if keyIndex == len(key) :
                keyIndex = 0
        
        else :
            translated.append (symbol)
    
    return ''.join (translated)
        
        
if __name__ == '__main__' :
    mode = input("Entrez le mode que vous voulez utiliser (encrypt ou decrypt) : ")
    message = input("Entrez le message à traduire : ")
    key = input("Entrez la clé de décrpytage : ")
    main (mode, message, key)