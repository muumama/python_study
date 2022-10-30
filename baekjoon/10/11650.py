import sys
n = int(sys.stdin.readline())
array = []
for j in range(n):
    [a,b] = map(int, sys.stdin.readline().split())
    array.append([a,b])
s_array = sorted(array)
for i in range(n):
    print(s_array[i][0], s_array[i][1])