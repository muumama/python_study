# 학생 답
s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

# 정답지
a = [3,2,4,2,5,2,4,3,1,2]

for i in range(len(s)): 
    #이름과 답안지 분리 
    s[i] = s[i].split(',') 
    #답안지 번호 별 분리 
    s[i][1] = list(map(int, s[i][1]))

def grader(s, a):
    for i in range(len(s)):
        score = 0
        for j in range(len(s[i][1])):
            if a[j] == s[i][1][j]:
                score += 1
        score = score*(100//len(a))
        s[i][1] = score
    s.sort(key= lambda x:x[1],reverse=True)
    for i in range(len(s)):
        print("학생: "+s[i][0]+" 점수: "+str(s[i][1])+"점"+str(i+1)+"등")
grader(s, a)
 
 