def isPrime(p):
    for j in range(2, int(1+p**0.5)):
        if p%j == 0:
            return False
    return True

s = 0
for n in range(2, 2 * 10**6):
    if isPrime(n):
        s += n

print(s)
