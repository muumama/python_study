#2675

num = int(input())

for i in range(num):
    r, s = input().split()
    for j in s:
        print(j*int(r),end='')
    print()
    