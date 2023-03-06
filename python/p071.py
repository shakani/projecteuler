'''
Use Farey Fractions to get the answer
https://en.wikipedia.org/wiki/Farey_sequence

Farey neighbor of c/d is a/b. Next neighbor is

(a+c)/(b+d)

'''

def next_rat(den = 8):
    a, b = 2, 5
    while b < den:
        a, b = a+3, b+7
    return a

N = 10**6
print(next_rat(5 + 7 * ((N - 5)//7)))
