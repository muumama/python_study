a = int(input())
b = []
for i in range(a):
  b.append(' ')

n = -1
for j in range(a):
  
  b[n] = "*"
  n = n-1
  print(''.join(b))
  