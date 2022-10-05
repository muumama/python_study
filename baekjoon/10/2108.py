#2108
import sys
from collections import Counter

n = int(sys.stdin.readline())
num_list = []
for i in range(n):
  num_list += [int(sys.stdin.readline())]
num_list.sort()

#산술평균
a = int(sum(num_list))
if a >= 0 :
  print(int(sum(num_list) / n + 0.5))
elif a < 0 :
  print(int(sum(num_list) / n - 0.5))

#중앙값
print(num_list[n//2])

#최빈값
cnt = Counter(num_list)
tmp = cnt.most_common()


if len(tmp) > 1:
  if tmp[0][1] == tmp[1][1]:
    print(tmp[1][0])
  else:
    print(tmp[0][0])
else:
  print(tmp[0][0])

#범위
print(max(num_list)-min(num_list))
