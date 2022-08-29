#4673


numbers = set(range(1, 10000))
remove_set = set()
for num in numbers :
    for n in str(num):
        num += int(n)
    remove_set.add(num)

self_numver = numbers - remove_set
for self_num in sorted(self_number):
    print(self_num)
    