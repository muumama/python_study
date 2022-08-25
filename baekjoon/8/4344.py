#4344
test_case = int(input())

case = []
for i in range(test_case):
  a = list(map(int,input().split()))
  n = a[0]
  del a[0]
  sum = 0
  smt = 0
  
  for score in a:
    sum += score
  average = sum/n
 
  for score in a:
    if score > average:
      smt += 1
    else:
      smt += 0
  pst = "{:.3f}%".format(smt/n*100)
  case.append(pst)
print(*case, sep='\n')
            
            