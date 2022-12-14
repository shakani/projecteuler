'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

def istri(s):
    n = 0.5*(-1 + (1 + 8*s)**0.5)
    return n == int(n)

def namescore(name):
    return sum([ord(c)-ord('A')+1 for c in name])

def istriname(name):
    return istri(namescore(name))

with open('p042_words.txt') as f:
    arr = (f.readlines()[0]).split(',')
    arr = [name.strip('\"') for name in arr]
    arr = [name for name in arr if istriname(name)]
    print(len(arr))
