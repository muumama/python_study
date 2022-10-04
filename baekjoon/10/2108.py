#2108
import numpy
n = int(input())
num_list = []
for i in range(n):
  num_list += int(input())
num_list.sort()
print(numpy.mean(num_list))
print(num_list[n//2])

#최빈값
print()


#범위
print(max(num_list)-min(num_list))