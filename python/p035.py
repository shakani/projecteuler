'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def erat(n): 
    arr = list(range(0,n+1))
    for i in range(2, int(n**0.5)+1):
        if arr[i]:
            j = i**2
            while j <= n:
                arr[j] = 0 
                j += i
    return [p for p in arr[2:] if p]

def circs(p, arr=[]): # only for p > 10
    if p in arr:
        return arr
    else:
        return circs(int(str(p)[1:] + str(p)[0]), arr + [p])

def odds(p):
    p_str = str(p)
    return '2' not in p_str and '4' not in p_str and '6' not in p_str and '8' not in p_str and '0' not in p_str

primes = erat(10**6)[4:] # start from 2 digit primes below 10**6
#primes = [p for p in primes if odds(p)] # only odd digit primes allowed
circulars = [2,3,5,7]

for p in primes[100:130]:
    for q in circs(p):
        if q not in primes:
            break

print(circulars)
