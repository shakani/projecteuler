'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

'''

from erat import erat # prime sieve I wrote

def isPrime(p):
    for d in range(2, int(2+p**0.5)):
        if p % d == 0:
            return False
    return True

def checker(n):
    primes = erat(n)
    for p in primes:
        x = ((n-p)/2)**0.5
        if x == int(x): # I've found n = p + 2x^2
            return False
    return n%2 == 1 and not isPrime(n)

for n in range(10, 10**4):
    if checker(n):
        print(n)
        break
