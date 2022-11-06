'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def ispalindrome(n):
    return n == int(str(n)[::-1])

def bispalindrome(n):
    b = bin(n)[2:]
    return b == b[::-1]

s = 0
for n in range(1, 10**6):
    if ispalindrome(n):
        if bispalindrome(n):
            s += n
print(s)
