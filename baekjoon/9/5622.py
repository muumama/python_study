#5622

alphabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
time = 0
for i in alphabet_list:
    for j in i:
        for k in word:
            if j == k:
                time += alphabet_list.index(i)+3
print(time)

