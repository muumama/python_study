import sys


h,m = map(int,sys.stdin.readline().split())
p = int(input())

if m + p >= 60:
#    h = h + (m+p)/60
    h += (m+p)/60
if h >= 24:
    h = h-24

m = (m+p)%60

print(int(h), int(m))
