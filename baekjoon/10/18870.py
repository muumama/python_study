#18870
import sys
n = int(input())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
#print(numbers)
num_set = set(numbers)
num_list = list(num_set)
num_list.sort()
num_dict = {}
for i in range(len(num_list)):
  num_dict[num_list[i]] = i

for i in numbers:
  print(num_dict[i],end=' ')
  
