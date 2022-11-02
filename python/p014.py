'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''
import sys

collatz_dict = {}

def c(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n + 1

def collatz(n, count=0):
    if n == 1:
        return count+1
    if n in collatz_dict:
        return count+collatz_dict[n]
    else:
        return collatz(c(n), count+1)

for i in range(1,int(sys.argv[1])): # populates dictionary
    collatz_dict[i] = collatz(i)

c_max = {'index': 0, 'chain length':0}
for m in collatz_dict:
    if collatz_dict[m] > c_max['chain length']:
        c_max['index'], c_max['chain length'] = m, collatz_dict[m]

#print(c_max)
print(c_max['index'])
