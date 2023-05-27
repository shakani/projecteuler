import time

def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Runtime: {round(time.time() - start, 6)}')
        return result

    return wrapper

@timed
def isPrime(p): 
    d = 2
    while d <= p**0.5:
        if p%d == 0:    
            return False
        d += 1
    return True

print(isPrime(97))
