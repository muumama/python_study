word = input().upper()
word_uni = list(set(word))

cnt_list = []
for i in word_uni:
    cnt = word.count(i)
    cnt_list += cnt
    
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))
    print(word_uni[max_index])
    
 # add comment



