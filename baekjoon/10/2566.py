#2566

max_list = []
ver_index_list = []
for i in range(9):
  a = list(map(int,input().split()))
  a_max = max(a)
  max_list.append(a_max)
  ver_index = a.index(a_max)
  ver_index_list.append(ver_index)
  
allmax = max(max_list)
wid_index = max_list.index(allmax)

print(allmax)
print(wid_index+1, ver_index_list[wid_index]+1)