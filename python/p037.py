'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

# Sieve of Eratosthenes

def erat(n): 
    arr = list(range(0,n+1))
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            j = i**2
            while j <= n:
                arr[j] = 0
                j += i
    return [p for p in arr[2:] if p]

# prime number theorem says \pi(x) ~ x/ln(x)
# can check that for x = 2E+5, the sieve is deep enough

primes = erat(10**6)

def ltruncate(p):
    if p < 10 and p in [2,3,5,7]:
        return True
    elif p in primes:
        return ltruncate(p//10)
    else:
        return False

def rtruncate(p):
    if p < 10 and p in [2,3,5,7]:
        return True
    elif p in primes:
        return rtruncate(int(str(p)[1:]))
    else:
        return False

def truncate(p):
    return ltruncate(p) and rtruncate(p)

c = 0
for p in primes[4:]:
    if truncate(p):
        c += p

print(c)
