#2869
import math
a = list(map(int, input().split()))

up = a[0]
down = a[1]
top = a[2]
day = (top-down)/(up-down)
print(math.ceil(day))