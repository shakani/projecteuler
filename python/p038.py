'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

'''

def isPandigital(n):
    return n > 10**8 and n < 10**9 and set(str(n)) == set('123456789')

def pandigitalMultiple(n):
    m = ''.join([str(n*k) for k in range(1,10)])
    return int(m[:9])

#u = 10**8
nmax, pmax, u = 0, 0, 10**4 # above 5 digit numbers, will never get n > 1

for n in range(u)[::-1]:
    p = pandigitalMultiple(n)
    if isPandigital(p) and p > pmax:
        pmax, nmax = p, n

print(pmax)
