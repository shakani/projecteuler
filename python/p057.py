from fractions import Fraction
from math import ceil, log10
from functools import lru_cache

def n_digits(n):
    return ceil(log10(n))

F = Fraction(1)

s = 0
for k in range(1, 10**3):
    F = Fraction(1 + 1/(1+F))
    if n_digits(F.numerator) > n_digits(F.denominator):
        s += 1

print(s)
