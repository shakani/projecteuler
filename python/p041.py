'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''
from itertools import permutations

# largest 1..m pandigital prime has upper bound of m = 7
# if m = 8, and p is 1..8 pandigital, then sum of digits of p is 8*(8+1)/2 = 36 = 0 (mod 3)
# meaning p is not prime (contradiction!)
# hence m is bounded above by 7
# use sieve of Eratosthenes to find primes up to 10**8 - 1

def isprime(n): # naive primality test
    for d in range(2, int(n**0.5 + 1)):
        if n%d == 0:
            return False
    return True

perms = permutations(list(range(1,8))) # only need to look at 7! = 5040 permutations (small)
perms = list(map(lambda perm: int(''.join([str(d) for d in perm])), perms)) # map permutation tuple to integer
perms = [p for p in perms if isprime(p)] # filter by primality
print(max(perms)) # print max
