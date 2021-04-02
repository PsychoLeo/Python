from sympy import primefactors

# prime factors return function


def prime_factors(n):
    '''input : a number
    output : a list of its prime factors '''

    return primefactors(n)

# Stack Overflow found program (upgraded to return all prime factors) ->
# [2, 2, 3, 3, 3] instead of [2, 3] for prime_factors (108) i.e.


def prime_facs(n):
    stored_n = n
    i = 2
    factors = []
    result = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)

    for k in factors:
        while stored_n % k == 0:
            stored_n //= k
            result.append(k)

    return result

# list multiplier


def multiply(l):
    assert 0 not in l, '0 in list'
    m = 1
    for i in l:
        m *= i
    return m


# using the archimede method ('crible' in french) - own program
# finding all primes untill n

def erath_prime(n):
    values = [i for i in range(3, n, 2)]
    k = 3
    while k**2 < n:
        for i in values:
            if i % k == 0 and i != k:
                values.remove(i)
        k += 1
    return [2] + values

def erath_sieve_gen (n, values=None, iterations=0) :
    if iterations == 0 :
        values = list(range(2,n+1))
    first = values[0]
    values = [i for i in values if i%first!=0]
    yield first
    yield from erath_sieve_gen(n+1, values, iterations+1)

initial_n = 2
def natural_numbers (n=initial_n) :
    yield n
    yield from natural_numbers(n+1)

def erath_sieve_genB (num_gen) :
    n = next(num_gen)
    yield n
    yield from erath_sieve_genB (i for i in num_gen if i%n!=0)