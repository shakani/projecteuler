'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

# sum of upper right diagonal is sum of odd squares ~ solved in poly time ~ n^3
# other diagonals are index shifted versions ~ same order polynomial
# just manually sum another layer of the square to get S(1), S(2), S(3), S(4)
# lagrange interpolation 
# S(1) = 1
# S(2) = 1 + 9 + 7 + 5 + 3 = 25
# S(3) = 101 (given)
# S(4) = S(3) + 49 + 43 + 37 + 31 = 261 
'''
43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31
'''

# WolframAlpha says
# S(n) = (16/3)n^3 - 6n^2 + (14/3)n - 3 

def S(n):
    return int((16/3)*n**3 - 6*n**2 + (14/3)*n - 3)

# for 1001 x 1001 grid, we have (2n-1) = 1001 --> n = 501

print(S(501))
