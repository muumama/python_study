#1929

m,n = map(int,input().split())

for num in range(m,n+1):

  if num == 1:
    continue
  for i in range(2,int(num**0.5)+1):
    if num%i == 0:
      break
  else :  
    print(num)