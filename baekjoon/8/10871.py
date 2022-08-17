import sys
a,b = map(int,sys.stdin.readline().split())
c = list(map(int,sys.stdin.readline().split()))
c = c[:a]
d = []
n = 0
for i in range(a):
  
  if c[n] < b:
    d.append(c[n])
  n = n + 1

print(*d)