'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

# is there an upper bound?
# max fifth power digit sum for a d-digit number is d*9^5
# when d ~ 5.5, we optimally hit max sum
# this means we can only have 5 digit numbers that satisfy our property

def dsum(n):
    return sum([int(d)**5 for d in str(n)])

s = 0
for n in range(2, 10**6):
    if dsum(n) == n:
        s += n

print(s)
