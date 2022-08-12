11021번
a= int(input())
import sys
n = 1
for i in range(a):
  b,c = map(int,sys.stdin.readline().split())
  d = b + c
  print(f'Case #{n}: {d}')
  n = n+1
