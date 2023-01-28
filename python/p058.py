'''
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

'''

# bottom right diagonal is odd perfect squares (2k-1)**2 up to L^2
# bottom left diagonal is (2k-1)**2 - (2k-2) = 4k^2 - 6k + 3
# top left is (2k-1)^2 - 2*(2k-2) = 4k^2 - 8k + 5
# top right is (2k-1)^2 - 3*(2k-2) = 4k^2 - 8k + 5


def isPrime(p):
    for d in range(2, int(2+p**0.5)):
        if p%d == 0:
            return False
    return True

def pRatio(L): # poly time of computing the ratio
    tot = 2*L-1
    pcount, L = 0, int((L+1)/2) # index of odd numbers used
    for k in range(2, L+1):
        for m in range(4):
            p = (2*k-1)**2 - m*(2*k-2)
            if isPrime(p):
                pcount += 1
    return pcount/tot

# experimentally found critical spiral size is somewhere between 2E+4 and 3E+4

def bSearch(pcrit): # binary search to find optimal spiral size
    lo, hi = 2E+4, 3E+4
    mid = lo + (hi-lo)//2
    while lo < hi:
        #print(lo, mid, hi)
        pnow = pRatio(mid)
        if pnow < pcrit: # spiral size too big since pRatio monotonically decreases
            hi = mid - 1
        else: # spiral size too small
            lo = mid + 1
        mid = lo + (hi-lo)//2
    return mid


print(bSearch(.1))
