#2581

m = int(input())
n = int(input())
num_list = []
for num in range(m,n+1):
    error = 0
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                error += 1
                break
        if error == 0:
            num_list.append(num)

if len(num_list) == 0:
    print(-1)
else:   
    print(sum(num_list))
    print(min(num_list))