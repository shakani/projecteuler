'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''

def d(n):
    divs = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            divs.append(i)
    for div in divs:
        if int(n/div) not in divs:
            divs.append(int(n/div))
    return sum(divs)-n

def amicablesum(u):
    amicables = []
    for i in range(2,u):
        if i not in amicables:
            d_i = d(i)
            if i == d(d_i) and i != d_i:
                amicables.append(i)
                amicables.append(d_i)
        else:
            continue
    return sum(amicables)

print(amicablesum(10000))
