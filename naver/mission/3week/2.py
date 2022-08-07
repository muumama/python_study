def rsp_advanced(games): #함수선언

    i = 1
    while i <= games: # while 조건문에서 game 수 보다 적게 출력
        import random
        computer = random.choice(("가위","바위","보"))

        my = input("나: ")
        print("컴퓨터: ", computer)

        if my == "가위":
            if computer == "가위":
                print(f"{i}번째 판 무승부")
            elif computer == "바위":
                print(f"{i}번째 판 나의 패배!")
            elif computer == "보":
                print(f"{i}번째 판 나의 승리!.")
        elif my == "바위":
            if computer == "가위":
                print(f"{i}번째 판 나의 승리!.")
            elif computer == "바위":
                print(f"{i}번째 판 무승부")
            elif computer == "보":
                print(f"{i}번째 판 나의 패배!")
        elif my == "보":
            if computer == "가위":
                print(f"{i}번째 판 나의 패배!")
            elif computer == "바위":
                print(f"{i}번째 판 나의 승리!.")
            elif computer == "보":
                print(f"{i}번째 판 무승부")

        i = i + 1
    print("나의전적")

games = int(input("몇 판을 진행하시겠습니까? : "))

rsp_advanced(games)
