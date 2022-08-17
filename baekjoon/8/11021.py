# 11021번
a = int(input())
for i in range(a):
  import sys
  b,c = map(int,sys.stdin.readline().split())  
  print(f'Case #{i+1}: {b} + {c} = {b+c}')