#2675
nums= int(input())
for i in range(nums):
    r,s = input().split()
    text = ''
    for j in s:
        text += int(r)*j
    print(text)
