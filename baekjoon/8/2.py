a = input()
b = input()

b1 = str(b)
#print(b[-1])
b2 = len(b1)

answer = 0
plus = 0
n = -1
while b2 != 0:
  plus = int(a)*int(b1[n])
  print(plus)
  answer = answer + plus*10**(-n-1)
  n = n - 1
  b2 = b2 - 1


print(answer)
