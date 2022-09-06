#2908

a, b = input().split()

a = list(str(a))
n = 1
a_reverse = []
for i in range(len(a)):
    a_reverse += a[-n]
    n = n + 1
    print(a_reverse)