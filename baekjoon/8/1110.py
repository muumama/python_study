#1110
num = int(input())
n=0
a = num

while True:
  num = (num%10)*10+(num//10+num%10)%10
  n = n + 1
  if num == a:
    print(n)
    break