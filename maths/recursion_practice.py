# list of numbers
def sum_list (l, val=0, i=0) :
    return val if i==len(l) else sum_list (l, val+l[i], i+1)

# sum of digits of a number
def sum_num (n, val=0, i=0) :
    return val if i==len(str(n)) else sum_num (n, val+int(str(n)[i]), i+1)
def sum_digits (n) :
    return 0 if n==0 else n%10+sum_digits(n//10)

# sum of n+(n-2)+(n-4)... untill n-x >= 0

def sum_suite (n) :
    return 0 if n <= 0 else n + sum_suite(n-2)

# list of numbers or lists - recursion

def sum_l (l, val=0, i=0, i2=0):
    if i==len(l):
        return val
    elif isinstance(l[i], list) and i2 < len(l[i]):
        if i2 == len(l[i])-1 :
            return sum_l (l, val+l[i][i2], i+1)
        return sum_l (l, val+l[i][i2], i, i2+1)
    else :
        return sum_l (l, val+l[i], i+1)

# list of numbers or lists - iteration

def sum_iter (l) :
    return sum([sum(i)if isinstance(i, list) else i for i in l])