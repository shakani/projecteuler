'''
Again use Farey Fractions (like p071).

Next fraction between a/b < c/d is (a+b)/(c+d)
Count these until we hit the upper bound

'''

fracs = [(1, 3), (1, 2)]

def iterate(arr, dmax):
    m = 0
    for i in range(len(fracs)-1):
        a, b = fracs[i][0], fracs[i][1]
        c, d = fracs[i+1][0], fracs[i+1][1]
        if b+d <= dmax:
            arr.insert(i+1, (a+c, b+d))
            m = max(m, b+d)
    return arr, m

def n_iterate(arr, n, dmax):
    max_den = 0
    while n > 0:
        arr, max_den = iterate(arr, dmax)
        n -= 1
    return arr, max_den

arr, _ = n_iterate(fracs, 600, 1000)
print(len(arr)-2)
