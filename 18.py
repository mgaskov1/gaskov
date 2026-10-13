# Ввод данных
a, b = map(float, input("Введите размеры отверстия A и B: ").split("x"))
c, d, e = map(float, input("Введите размеры кирпича C, D и E: ").split("x"))
hole1, hole2 = a, b
if hole1 > hole2:
    hole1, hole2 = hole2, hole1
b1, b2, b3 = c, d, e
if b1 > b2:
    b1, b2 = b2, b1
if b2 > b3:
    b2, b3 = b3, b2
if b1 > b2:
    b1, b2 = b2, b1
if b1 <= hole1 and b2 <= hole2:
    print("да")
else:
    print("нет")
