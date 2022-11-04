'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''

import numpy as np

def namescore(name):
    return sum([ord(c)-ord('A')+1 for c in name])

with open('p022_names.txt') as f: # cleans & sorts names, then maps names to name score
    names = f.readline().split(',')
    names = list(map(lambda n: n[1:-1], names))
    names.sort()
    names = np.array(list(map(namescore, names)))

indices = np.array(list(range(1,len(names)+1))) # 1-indexed indices for the name array

print(np.dot(names, indices)) # return dot product
