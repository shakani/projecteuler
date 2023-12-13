u = 10000

hashmap = {}

for i in range(u):
    n = ''.join(sorted(str(i**3)))
    hashmap[n] = hashmap.get(n, []) + [i]
    if len(hashmap[n]) == 5:
        #print(hashmap[n], min(hashmap[n])**3)
        print(min(hashmap[n])**3)
        break
