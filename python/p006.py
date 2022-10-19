# sum square difference
# sum of squares is 1^2 + 2^2 + ... + n^2
# square of sum is (1 + 2 + ... + n)^2
# find difference between sum of squares and square of sum

def sumOfSquares(n):
    return n*(n+1)*(2*n+1)/6

def squareOfSum(n):
    return (n*(n+1)/2)**2

def ans(n):
    return int(squareOfSum(n) - sumOfSquares(n))

print(ans(100))
