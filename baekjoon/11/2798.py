from itertools import permutations

n, m = map(int, input().split())

num = list(map(int, input().split()))
permutationArray = permutations(num, 3)
ans = 0
for i in permutationArray:
    if(m+1 > sum(i)):
        ans = max(ans, sum(i))
    
print(ans)
