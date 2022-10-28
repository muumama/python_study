n = int(input())
area = [[0] * 100 for _ in range(100)]
for _ in range(n):
  a,b = map(int, input().split())
  for i in range(a,a+10):
    for j in range(b,b+10):
      area[i][j] = 1

cnt = 0
for k in area:
  cnt += k.count(1)
   
print(cnt)
