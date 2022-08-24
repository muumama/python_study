#8958

a = int(input())

b = []

for i in range(a):
    b += input()

    score = 0
    n = 0
    score_plus = 0
    score_list = []
    for j in range(len(b[i])):    
        
        if b[i][j] == "O":
            if b[i][j] == b[i][n]:
                score_plus = score_plus + 1
            else:
                score_plus = 1
        else:
            score_plus = 0
        score = score + score_plus
        n = j - 1
    score_list.append(score)
print(score_list)
                    
                
                
            
            
            