#5597
a = []
for i in range(1,31):
  a.append(i)

for j in range(28):
  a.remove(int(input()))
a.sort()
for k in range(2):
  print(a[k])