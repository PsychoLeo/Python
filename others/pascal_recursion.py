import pprint

def recursive (n, s=[[1]]) :
    if n==0 :
        return s
    else :
        s.append([1] + [s[-1][i]+s[-1][i+1] for i in range (len(s[-1])-1)] + [1])
        return recursive(n-1, s)

pprint.pprint(recursive(5))
pprint.pprint(recursive(10))

# def iterative (n) :
#     l = [['1\n']]
#     for i in range (1, n+1) :
#         l.append (['1'] + [str(int(l[-1][j])+int(l[-1][j+1])) for j in range (i-1)] + ['1\n'])
#     print (''.join([' '.join(i) for i in l]))