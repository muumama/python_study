#3052
num = []
cnt = 0
for i in range(10):
  num.append(int(input())%42)


for i in range(42):
    if i in num:
        cnt += 1
    else:
        pass
    
print(cnt)