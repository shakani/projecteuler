'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

u = 28123 # upper bound above which all numbers can be written as sum of 2 abundants

def d(n): # sum of proper divisors of n
    divs = []
    for i in range(1, 1 + int(n**0.5)):
        if n%i == 0:
            divs.append(i)
    for d in divs:
        if int(n/d) not in divs:
            divs.append(int(n/d))
    return sum(divs)-n

abundants = []
for i in range(1, u):
    if i < d(i):
        abundants.append(i)

abundants.sort()

two_abs = []

for i in abundants:
    for j in abundants:
        s = i+j
        if s > u:
            break
        else:
            two_abs.append(i+j)

two_abs = list(set(two_abs)) # list of all numbers below u which CAN be written as sum of 2 abundants

print(int(u*(u+1)/2 - sum(two_abs)))
