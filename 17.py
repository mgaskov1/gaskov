import math
R = 6.5
a,b=map(int,input().split("x"))
h = math.sqrt(a ** 2 + b ** 2) / 2
if h <= R:
    print("да")
else:
    print("нет")
