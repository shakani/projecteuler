'''
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
'''

from functools import reduce
from itertools import permutations

keylog = []

with open('p079_keylog.txt', 'r') as f:
    for line in f:
        keylog.append(line.strip('\n'))

def check_passcode(pwd_n, g):
    pwd, guess = str(pwd_n), str(g)
    i = 0
    for idx, el in enumerate(pwd):
        if el == guess[i]:
            i += 1
        if i == 3:
            return True
    return False

def check_keylog(pwd):
    return all([check_passcode(str(pwd), guess) for guess in keylog])

# lower bound for number is 10236789
# search up to 98763210

pwds = list(map(lambda p: ''.join(p), permutations(str(10236789)))) # generate list of all possible permutations of lower bound 

good_pwds = list(filter(check_keylog, pwds)) # filter all permutations by whether they match the keylog 

print(good_pwds[0]) # only one answer it turns out
