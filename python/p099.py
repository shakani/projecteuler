'''
Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

'''

from math import log

i, m, c = 0, 0, 0

def myexp(arr): 
    b, e = arr
    return e*log(b)

with open('p099_base_exp.txt') as f: # just do the exponent in log
    myarr = list(map(myexp, [list(map(int, line.strip('\n').split(','))) for line in f.readlines()]))
    print(myarr.index(max(myarr))+1)
