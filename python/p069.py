'''
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

'''

from functools import lru_cache
from erat import erat # sieve of eratosthenes
import sys

N = int(sys.argv[1])
#primes = erat(10**N)
#primes = primes

'''
def phi(x):
    totient = x
    factors = [p for p in primes[:x] if x%p == 0]
    for f in factors:
        totient -= totient//f
    return totient
'''

def isPrime(p):
    for d in range(2, int(1+p**0.5)):
        if p%d == 0:
            return False
    return True

@lru_cache
def maxratio(u = 100):
    nmax, rmax = 0,0
    for n in range(2, u):
        # compute totient
        totient = n
        for p in range(2, n):
            if isPrime(p) and n%p == 0:
                totient -= totient//p
        # now I have the totient
        r = totient/n
        if r > rmax:
            nmax, rmax = n, r
    return nmax, rmax

print(maxratio(10**N))
