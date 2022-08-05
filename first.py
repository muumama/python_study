def greeting(input):
    try:
        name = int(input)
    except:
        name = -1
        print("Please input your name")

    return "Hello" + name

print(greeting("1110"))
