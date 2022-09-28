num = 10001
a = [False,False]+[True]*(num+1)
for j in range(2,int(num**0.5)+1):
    if a[j] == True:
        for k in range(j+j,num+1,j):
            a[k] = False


n =int(input())

for i in range(n):
    number = int(input())
    ans1 = number//2
    ans2 = number//2
    while ans1 > 0:
        if a[ans1] and a[ans2]:
            print(ans1, ans2)
            break
        else:
            ans1 -= 1
            ans2 += 1
            

