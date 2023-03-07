'''
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
'''

def rect(a, b, c = 0): # counts number of rectangles for a x b grid
    return int((a*(a+1)*b*(b+1))//4) - c

U = int(2e6) # upper bound; target I want closest to rect(a, b)
x = int((4*U)**0.25) + 1 # approximate lower bound where square of this side length has U rectangles in it (a = b ~ a+1)

a_min, b_min = 0, 0
r_min = 0

for a in range(1, 2*x): # go to 2x just in case
    for b in range(a, 2*x):
        r = rect(a, b)
        if abs(r - U) < abs(r_min - U):
            a_min, b_min, r_min = a, b, r

#print(a_min, b_min, r_min, a_min*b_min)
print(a_min*b_min)
