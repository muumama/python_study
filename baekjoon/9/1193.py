num = int(input())
line = 1
num_max = 1
while num_max < num:
    line = line + 1
    num_max = num_max + line

a = num_max - num
if line % 2 == 0:
    print(line - a,'/',1 + a, sep='')
else :
    print(1 + a,'/',line - a, sep='')