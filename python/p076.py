'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

'''
import sys
def partitions(n):
    parts = [1]+[0]*n
    for t in range(1, n+1):
        for i, x in enumerate(range(t, n+1)):
            parts[x] += parts[i]
    return parts[n] - 1 # don't count trivial partition

print(partitions(int(sys.argv[1])))
