'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

'''

def pcounter(p):
    s = 0
    for a in range(1, p):
        for b in range(a, p):
            if a**2 + b**2 == (p-(a+b))**2:
                s += 1
    return s

pmax, cmax = 0, 0
for p in range(3, 1000):
    cnow = pcounter(p)
    if cnow > cmax:
        pmax, cmax = p, cnow

print(pmax, cmax)
