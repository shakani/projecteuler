from sympy.ntheory.factor_ import totient as totient

'''
Farey sequences:

|F_n| = |F_{n-1}| + phi(n)

where phi is the totient function
'''

def F(n):
    Fn  = 1
    for m in range(1, int(n)+1):
        Fn += totient(m)
    return Fn

print(F(1e6) - 2)
# subtract 2 to exclude 0, 1
