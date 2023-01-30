'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''

from math import ceil, log10
from functools import reduce

def n_digits(n):
    return ceil(log10(n))

def isPerm(x, m):
    return reduce(lambda x, y: x == y, [sorted(str(x*k)) for k in range(1,m+1)])


for x in range(1, 6):
    for j in range(10**x, 1 + (10**(x+1) - 1)//6): # limits search based on number of digits matching
        if sorted(str(j)) == sorted(str(2*j)) == sorted(str(3*j)) == sorted(str(4*j)) == sorted(str(5*j)) == sorted(str(6*j)):
            print(j)
            break
