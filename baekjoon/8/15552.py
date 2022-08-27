import sys
aab = int(input())

for i in range(aab):
  b,c = map(int, sys.stdin.readline().split())
  total = b + c + 0
  print(total)
