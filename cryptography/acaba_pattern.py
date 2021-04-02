from string import ascii_uppercase

def abacaba_pattern(n):
    assert n > 0
    if n == 1 :
        return 'A'
    else :
        return abacaba_pattern(n-1) + ascii_uppercase[n-1] + abacaba_pattern(n-1)