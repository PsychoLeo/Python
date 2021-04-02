from string import ascii_lowercase, ascii_uppercase

def atbash (txt) :
    equivalent = {ascii_lowercase[i]:ascii_lowercase[25-i] for i in range (len(ascii_lowercase))}
    equivalent.update({ascii_uppercase[i]:ascii_uppercase[25-i] for i in range (len(ascii_uppercase))})
    print (equivalent)
    return ''.join([equivalent[i] if i in equivalent else i for i in txt])

def convert_cartesian(x, y):
    l = []
    for i in range (len(x)) :
        l.append ([x[i], y[i]])
    return l