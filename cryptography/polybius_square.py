def polybius (text) :
    
    '''input : a message to encrypt / decrypt with the polybius square
    ouput : this message decrypted / encrypted'''
    
    square = ['abcde', 'fghik', 'lmnop', 'qrstu', 'vwxyz']
    
    if text[0].isdigit () : # decrypt
        k = 0
        txt = []
        while k < len(text) :
            if text[k].isdigit () :
                txt.append (text[k:k+2])
                k += 2
            else :
                txt.append (' ')
                k += 1
        for i in range (len(txt)) :
            if txt[i] != ' ' :
                txt[i] = square[int(txt[i][0])-1][int(txt[i][1])-1]
        
    else : # encrypt
        text = text.lower()
        text = [i for i in text if i.isalpha() or i == ' ']
        txt = []
        for i in text :
            if i == ' ' :
                txt.append (' ')
            elif i == 'j' :
                txt.append ('24')
            else :
                for col in range (len(square)) :
                    if i in square[col] :
                        a, b = col + 1, square[col].index(i) + 1
                        txt.append (str(a) + str(b))
    
    return ''.join (txt)