
while True:

    n = int(input())
    a = [True] * (2*n + 1)
    m = int((2*n)**0.5)
    if n == 0:
        break
    elif n == 1:
        print(1)
        continue
    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, 2*n + 1, i):
                a[j] = False

    else:
        print(len([i for i in range(n+1, 2*n + 1) if a[i] == True]))
