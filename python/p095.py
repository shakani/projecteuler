'''
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.

'''

u = 10**2

def dsum(n):
    s = 1
    for d in range(2, int(2+n**0.5)):
        if n%d == 0:
            s += d+n//d
    return s

divsums = {n:dsum(n) for n in range(1, u)} # takes 32s to memoize all divsums
print('Memoized')

def amicable_chain(n):
    m, chain = n, []
    while n not in chain:
        d = divsums[m]
        chain.append(d)
        m = d
    return chain

def longest_chain(u):
    ind, chain = 0, []
    for n in range(1, u):
        if n in chain:
            continue
        else:
            ac = amicable_chain(n)
            if len(ac) > len(chain):
                ind, chain = n, ac
    return ind, len(chain)

print(longest_chain(u))
