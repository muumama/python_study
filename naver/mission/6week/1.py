import sys
a = int(input())

for i in range(a):
  b,c = map(int, sys.stdin.readline().split())
  total = b + c + 0
  print(total)
