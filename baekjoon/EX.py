def d(n):
    n = n +sum(map(int, str(n)))
    return n

nonselfnum = set()

for i in range(1, 10001):
    nonselfnum.add(d(i))
    
for j in range(1, 10001):
    if j not in nonselfnum:
        print(j)
