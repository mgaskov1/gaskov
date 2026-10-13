n = int(input("Введите количество кнатов: "))
g = n // 493
r= n % 493
sickles = r // 29
knuts = r % 29
if g > 0:
    print(g,"галлеон(ов)")
if sickles > 0:
    print(sickles,"сиклей")
if knuts > 0:
    print(knuts,"кнат(ов)")
