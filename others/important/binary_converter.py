from string import ascii_lowercase

def binary (num) :
    r = ''
    while num != 0 :
        if num % 2 == 0 :
            r += '0'
            num = num//2
        else :
            r += '1'
            num = num//2
    print (r[::-1])

'''if __name__ == '__main__' :
    num = int(input('Enter the number you want to convert into binary form : '))
    binary (num)'''
    
    
def binary_new (n) :
    return bin(n)[2:]

alph = list(ascii_lowercase)

ascii_convert = {alph[i]:i+97 for i in range (len(alph))}

def ascii_text_binary (txt) :
    return ' '.join([binary_new(i) for i in [ascii_convert[i] for i in txt]])


