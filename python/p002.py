# Problem 2

a, b, s = 1, 2, 0

while b <= 4*10**6:
    if b%2 == 0:
        s += b
    a, b = b, a+b

print(s)
