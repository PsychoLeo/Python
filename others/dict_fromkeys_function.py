def sort_remove_duplicates (l) : # sort and removes duplicates
    d = {}
    for i in l :
        if i not in d :
            d[i] = 0
    return sorted (d.keys())

def remove_duplicates_keeporder (l) : # remove duplicates and keeporder
    nl = []
    for i in l:
        if i not in nl:
            nl.append (i)
    return nl