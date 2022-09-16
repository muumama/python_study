#2775
num = int(input())

for i in range(num):
  k = int(input()) # 층 수
  n = int(input()) # 호실
  count_p = 0 # 사람 수
  count_list = []
  for b in range(n):
    count_p = count_p + 1
    count_list.append(count_p)
    #print(count_list)
  for a in range(k):
    for b in range(1, n):
      count_list[b] += count_list[b-1] 
      #print(count_list)
  print(count_list[-1])