#25870
nlist = []
for i in range(5):
    n = int(input())
    nlist.append(n)
print(int(sum(nlist)/5))
nlist.sort()
print(nlist[2])