while True:
    n = int(input())
    if n == 0:
        break
    sosu = 0
    for i in range(n,2*n+1):
        if i == 1:
            continue
        elif i == 2:
            sosu += 1
            continue
        for j in range(2,int(i**0.5+1)):
            if i % j == 0:
                break
        else:
            sosu += 1
    print(sosu)

