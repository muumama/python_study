h,m = map(int,input().split())
p = int(input())

if m + p > 60:
    h = h + (m+p)/60
    m = (m+p)%60
else:

    m = m+p

print(h, m)
