#10818
import sys
a = int(input())
b = list(map(int,sys.stdin.readline().split()))
b = b[:a]
#print(b)
n = 1
max = b[0]
min = b[0]

for i in range(a-1):
  if max < b[n]:
    max = b[n]
  if min > b[n]:
    min = b[n]
  n = n + 1
print(min, max)