#2562

num = []
for i in range(9):
  num.append(int(input()))

n = 0
b = num[0]
for i in range(len(num)):
  if b <= num[n]:
      b = num[n]
  n = n + 1

print(b,
      n-1)
