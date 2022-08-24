#1546
import sys
a = int(input())

score = list(map(int,sys.stdin.readline().split()))

max_score = max(score)
n = 0
for i in range(a):
    score[i] = score[i]/max_score*100
    n = n + score[i]
print(n/a)
