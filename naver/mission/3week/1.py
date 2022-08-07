def gugudan(number):
    print(f"{number}단")
    i = 1
    while number*i <= 50:
        print(f"{number}X{i}={number*i}")
        i = i + 2
number = int(input("몇 단? : "))
gugudan(number)
