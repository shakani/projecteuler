# Problem 4

def isPalindrome(x):
    return x == int(str(x)[::-1])

m = 0

for i in range(1000)[::-1]:
    for j in range(1000)[::-1]:
        p = i*j
        if isPalindrome(p):
            m = max(m, p)

print(m)
