import random
computer = random.choice(("가위","바위","보"))
#rsp == rock scissors paper

my = input("나: ")  # 입력받은 값을 my 에 넣어준다.
print("컴퓨터: ", computer) # 컴퓨터가 어떤 값을 갖고있는지 출력해준다.

if my == "가위": # 내가 가위를 냈을 때
    if computer == "가위":
        print("무승부")
    elif computer == "바위":
        print("컴퓨터 패배")
    elif computer == "보":
        print("이겼습니다.")
elif my == "바위": # 내가 바위를 냈을 때
    if computer == "가위":
        print("이겼습니다.")
    elif computer == "바위":
        print("무승부")
    elif computer == "보":
        print("컴퓨터 패배")
elif my == "보": # 내가 보를 냈을 때
    if computer == "가위":
        print("컴퓨터 패배")
    elif computer == "바위":
        print("이겼습니다.")
    elif computer == "보":
        print("무승부")

'''
import random
computer = random.randint(0,2)

#rsp == rock scissors paper
my = int(input("나 : "))
print("컴퓨터 :", computer)

if my == 0 :
    if computer == 0 :
        print("무승부")
    elif computer == 1 :
        print("컴퓨터 승리")
    elif computer == 2 :
        print("컴퓨터 패배")
if my == 1 :
    if computer == 0 :
        print("컴퓨터 패배")
    elif computer == 1 :
        print("무승부")
    elif computer == 2 :
        print("컴퓨터 승리")
if my == 2 :
    if computer == 0 :
        print("컴퓨터 승리")
    elif computer == 2 :
        print("컴퓨터 패배")
    elif computer == 3 :
        print("무승부")
        '''
