'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?


'''

from functools import lru_cache

def erat(n): # prime sieve
    arr = list(range(0,n+1))
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            j = i**2
            while j <= n:
                arr[j] = 0 
                j += i
    return [p for p in arr[2:] if p]

def isPrime(p):
    for j in range(2, int(2+p**0.5)):
        if p%j == 0:
            return False
    return True

def consum(arr, u = 10**6):
    pmax, wmax, l = 0, 0, len(arr)
    for w in range(2, min(10**3, l))[::-1]:
        wsums = [sum(arr[i:i+w]) for i in range(l-w)]
        for s in wsums:
            if isPrime(s) and s <= u: # s is prime
                return s, w
    return None

primes = erat(10**4) # primes below 10**2
print(consum(primes))
