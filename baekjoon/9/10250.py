#10250
num = int(input())

for i in range(num):
  h,w,n = list(map(int, input().split()))

  floor = n%h 
  room_number = 1 + n//h
  if floor == 0:
    floor = h
    room_number = n//h
  
  print(floor*100+room_number)