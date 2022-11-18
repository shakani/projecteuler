'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
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
