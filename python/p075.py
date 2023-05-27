def singular(p):
    cnt = 0
    for a in range(1, p):
        for b in range(a+1, p-a): # only one of a, b is even
            if a**2 + b**2 == (p-(a+b))**2:
                cnt += 1
                if cnt > 1:
                    return False
    return cnt == 1 
