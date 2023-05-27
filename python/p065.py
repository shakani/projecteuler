from fractions import Fraction
import sys

def continuedFraction(arr): # return continued fraction of a given array
    f = 0
    for digit in arr[::-1]:
        f += digit
        f = Fraction(1, f)
    return Fraction(1, f)

def eulerConvergent(k): # generates k-th order continued fraction array to approximate e 
    arr = [2]
    m = 1
    while k > m:
        arr += [1, 2*m, 1]
        m += 1
    return arr[:k]

def eulerFraction(k): # returns k-th order continued fraction to approximate e
    return continuedFraction(eulerConvergent(k))

def digitSum(n): # returns digit sum of n
    return sum([int(d) for d in str(n)])

k = int(sys.argv[1])

print(digitSum(eulerFraction(k).numerator))
