#8958

a = int(input())
score_list = []

for i in range(a):
    b = input()

    score = 0
    score_plus = 0

    for j in b:    
        if j == "O":
            score_plus += 1
            score += score_plus
        else:
            score_plus = 0
    #print(score)
    score_list.append(score)
    
print(*score_list, sep='\n')
                    
                
                
            
            
            