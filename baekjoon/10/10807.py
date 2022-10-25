#2738

n = int(input())
nums = list(map(int, input().split()))
nums_dict = {}
for i in nums:
  if i in nums_dict:
    nums_dict[i] += 1
  else:
    nums_dict[i] = 1

print(nums_dict[int(input())])