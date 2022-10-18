# Largest prime factor of 600851475143

n = 600851475143

def isPrime(x):
    for j in range(2, int(x**0.5) + 1):
        if x%j == 0:
            return False
    return True


for i in range(int(n**0.5)+1)[::-1]:
    if n%i == 0:
        if isPrime(i):
            print(i)
            break
