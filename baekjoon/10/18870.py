#18870
import sys
n = int(intput())
numbers = map(int, sys.stdin.readline().split())
num_set = set(numbers)
num_list = list(num_set)
num_dict = {}
for i in range(len(num_list)):
  num_dict[numlist[i]] = i

for i in numbers:
  print(num_dict[i],end='')
  
