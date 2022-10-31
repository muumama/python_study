#11651
import sys
n = int(sys.stdin.readline())
array = []
for i in range(n):
    [a,b] = map(int, sys.stdin.readline().split())
    array.append([b,a])
s_array = sorted(array)
for i in range(n):
    print(s_array[i][1], s_array[i][0])