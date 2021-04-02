l = [1, 5, 11, 13, 17, 19, 23]
sol = [[None]*len(l) for _ in range (len(l))]
print ('n\m', end = ' | ')
for i in l :
    print (i, end = ' | ')
for m in l :
    print ()
    print (m, end = ' | ')
    for n in l :
        print ((m*n)%24, end = ' | ')
print ()