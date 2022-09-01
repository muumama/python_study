#2675
num = int(input())
for i in range(num):
    r,s = input().split()
    text = ''
    for j in s:
        text += int(r)*j
    print(text)
