def make_comma(number):
    number = str(number) # int를 str으로 변환
    length = len(number) # 숫자의 길이
    num_comma = length // 3 # 3으로 나눠서 찍어야하는 콤마의 개수 구하기
    if length % 3 ==0:
        num_comma = num_comma -1 # 길이가 3으로 나눠질 경우 -1

    new_number = "" # 새로운 숫자를 담을 변수 생성
    n = -1 # 인덱스를 거꾸로 가야하기 때문에 -1
    while num_comma != 0: # 콤마를 다 찍을 때까지 반복
        new_number = number[n] + new_number
        if  n % 3 == 0:
            new_number = "," + new_number
            num_comma = num_comma - 1
        n = n - 1
		# 콤마를 다 찍고 남은 앞의 숫자를 더해주면 완성

    print(number[:n+1]+new_number)

number = int(input("숫자를 입력하세요:"))
make_comma(number)
