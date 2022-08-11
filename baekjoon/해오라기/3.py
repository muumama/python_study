a,b = map(int,input().split())

0 <= a <= 24
0 <= b <= 60

if b-45 < 0:
  b = 60+b-45
  if a-1 < 0:
    a = 24 - 1
  else:
    a = a-1

elif b-45 > 0:
  b = b-45

print(a, b)
