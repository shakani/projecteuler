'''
5 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

# is there an upper bound on numbers which satisfy this property?
# for d digits with all 9s, the sum is d*9!
# that number would be 10^d - 1
# numerically solving for d with WolframAlpha gives d ~ 6.3
# only need to search up to 6 digit numbers

def fact(n, nfact=1):
    if n <= 1:
        return nfact
    else:
        return fact(n-1, n*nfact)

facts = [fact(d) for d in range(10)] # memoize factorial of digits so I don't have to keep computing them

def dfactsum(n, s=0):
    if n < 10:
        return s+facts[n]
    else:
        return dfactsum(n//10, s+facts[n%10])

s = 0
for n in range(3, 10**7):
    if n == dfactsum(n):
        s += n

print(s)
