n = int(input())
words = []
for i in range(n):
    words.append(input())

wordss = list(set(words))
wordss.sort()
wordss.sort(key=len)

for i in wordss:
    print(i)