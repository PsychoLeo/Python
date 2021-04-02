def scientif (num, cs=3) :
    '''input : a number as a string
    output : this number printed out in scientific notation'''
    isneg, isinf_one = '-' in num, eval(num.replace('.', '')) <= 1
    num = num.replace ('-', '')
    power = 0
    while eval(num) >= 10 :
        num = str(eval(num)/10)
        power += 1
    num = str(round(float(num), cs)) + f'*10^{power}'
    print('-'+num) if isneg else print(num); return None