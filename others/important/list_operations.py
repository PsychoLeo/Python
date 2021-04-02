##### Sorting lists #########

from more_itertools import unique_everseen


def advanced_sort(lst):
    return [[i for j in range(lst.count(i))] for i in sorted(set(lst), key=lambda x: lst.index(x))]

#############################################


''' def advanced_sort (lst) :
    res = []
    group = []
    for i in lst :
        for j in range (lst.count(i)) :
            group.append (i)
            print (group)
    res.append (group)
    group.clear ()
        
    return res '''

#############################################


def sort_list(l):
    result = []
    if len(l) == 0:
        return []
    else:
        for i in range(len(l)):
            result.append(min(l))
            l.remove(min(l))
    return result

###### ADDING LISTS ########


def add(m1, m2):
    l = []
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            l.append(m1[i][j] + m2[i][j])
    return l

####### Multiplying lists #########


def multiple(l):
    m = 1
    for i in (l):
        m = m * i
    return m

######## Converting sympy FiniteSet into Set #######


def sympy_sets(r):
    par = str(r).index('(')
    replaced = str(r).replace('(', '{')
    replaced = replaced.replace(')', '}')
    return eval(replaced[par:])


###### List without duplicates and ordered as initially #######

def order(l):
    m = {}
    for i in l:
        m[i] = None
    return list(m.keys())
