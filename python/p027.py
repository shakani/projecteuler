'''
https://projecteuler.net/problem=27
'''

from erat import erat # sieve of eratosthenes

def p(a, b, n):
    return n**2 + a*n + b

def isprime(n):
    for d in range(2, int(1 + n**0.5)):
        if n%d == 0:
            return False
    return True

primes = set(erat(2001000)) # upper bound of primes I need
