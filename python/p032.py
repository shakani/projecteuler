'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

from itertools import permutations

args = ['*','==','1','2','3','4','5','6','7','8','9']

tries = list(map(lambda p: ''.join(p), permutations(args)))

def myeval(p):
    try:
        return eval(p)
    except:
        return None

prods = []

for t in tries:
    if t[0] not in ['*', '=='] and t[-1] not in ['*', '==']:
        if myeval(t):
            p1, p2 = t.split('==')
            prods.append(eval(p1))
    else:
        continue

prods = list(set(prods))
print(sum(prods))
