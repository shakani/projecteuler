'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 
.

In general, 
 
, where , , and .

It is not until , that a value exceeds one-million: 
.

How many, not necessarily distinct, values of 
 for , are greater than one-million?


'''
import numpy as np
from scipy.special import binom

u = 100

all_binoms = np.zeros((u,u))
for n in range(1,u+1):
    for r in range(1,u+1):
        all_binoms[n-1][r-1] = binom(n,r)

print(all_binoms[all_binoms > 10**6].size)
