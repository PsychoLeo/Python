def gcd(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    solution = False

    while not solution:

        if a > b:
            if a % b != 0:
                b = a % b
                gcd(a, b)
            else:
                return b
                solution = True
        else:
            if b % a != 0:
                a = b % a
                gcd(a, b)
            else:
                return a
                solution = True


def pgcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
