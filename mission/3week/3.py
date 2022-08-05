def find_even_number(n, m):
    middle_number = (n+m)/2
    for i in range(n,m+1):
        if i % 2 == 0:
            print(str(i)+" 짝수")
            if i == middle_number:
                print(str(i)+" 중앙값")

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n, m)
