#1065
n = input()
num_han = list(map(int,str(n)))
num = 0
for i in range(int(n)+1):
    if i <= 100:
        num += 1 
    else:
        if num_han[0] - num_han[1] == num_han[1] - num_han[2]:
            num += 1
print(num)
