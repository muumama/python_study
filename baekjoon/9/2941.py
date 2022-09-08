#2941

cra = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()

for i in cra:
    word = word.replace(i,'*')
print(len(word))