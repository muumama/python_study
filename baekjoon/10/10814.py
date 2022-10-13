#10814

n = int(input())
j_list = []

for i in range(n):
  a,b = input().split()
  j_list.append((int(a),b))
j_list.sort(key=lambda x:x[0])

for i in j_list:
  print(i[0],i[1])