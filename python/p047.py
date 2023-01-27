'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''
from functools import lru_cache
from functools import reduce
from erat import erat

def primeFactors(n):
    #divs = []
    divs = 0
    for div in range(2, int(1+n**0.5)):
        if n%div == 0:
            #divs.append(div)
            divs += 1
            while n%div == 0:
                n /= div
    if n != 1:
        divs += 1
    return divs

@lru_cache
def pFinder(upper, k):
    for n in range(2, upper):
        if reduce(lambda x,y: x and y, [primeFactors(n+i)==k for i in range(k)]):
            return n
    return False

print(pFinder(2*10**5, 4))
