#4673

def d(n):
    n = n +sum(map(int, str(n)))
    return n

nonselfnum = set()

for i in range(1, 10001):
    nonselfnum.add(d(i))
    
for j in range(1, 10001):
    if j not in nonselfnum:
        print(j)


'''
numbers = set(range(1, 10000))
remove_set = set()
for num in numbers :
    for n in str(num):
        num += int(n)
    remove_set.add(num)

self_number = numbers - remove_set
for self_num in sorted(self_number):
    print(self_num)
'''
