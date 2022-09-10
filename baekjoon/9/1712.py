#1712

a, b, c = map(int,input().split())

if b >= c:
    print(-1)
else:
    print(int(b/(c-b)+1))
