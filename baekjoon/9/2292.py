#2292

# 1 - 7 - 19 - 37 - 61

num = int(input())

count_path = 1
n = 1
while n < num:
    n = n + 6*count_path
    count_path = count_path + 1
    
print(count_path)
