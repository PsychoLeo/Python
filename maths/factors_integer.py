# finding the factorials of an integer

def factors (b) :
    l = []
    for i in range (1, b+1) :
        if b % i == 0 :
            l.append (i)
    print (l)
            
if __name__ == '__main__' :
    try :
        b = int(input('Input the integer from which you want to get the factors : '))
        if b > 0 :
            factors (b)
        else :
            print ('please enter a positive integer')
    except ValueError :
        print ('please enter an integer')

# book version :

def factors (b) :
    for i in range (1, b+1) :
        if b % i == 0 :
            print (i)
            
if __name__ == '__main__' :
    b = input('your number please : ')
    b = float (b)
    if b > 0 and b.is_integer () :
        factors(int(b))
    else :
        print ('please enter a positive integer')
        
from functools import reduce

def factorial (n) :
    return reduce (lambda x,y : x*y, range (1,n+1))

