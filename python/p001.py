# Project Euler Problem no 1
# 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# 
# Find the sum of all the multiples of 3 or 5 below 1000.

'''
# old way; slow
s = 0
for i in range(1000):
    if i%3 == 0 or i%5 == 0:
        s += i

print(s)
'''

# multiples of 3 below 1000:
# 3 + 6 + ... + 999 = 3(1 + 2 ... + 333) = 3(1 + 2 + ... + 1000//3)
# multiples of 5 below 1000:
# 5 + 10 + ... + 1000 = 5(1 + 2 + ... + 200) = 5(1 + 2 + ... + 1000//5)

print(int(3*(1000//3)*(1000//3 + 1)/2 + 5*(1000//5)*(1000//5 + 1)/2))
