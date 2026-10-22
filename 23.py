n = int(input("Введите порядковый номер цифры меньше 494: "))

if n == 1:
    digit = 0
else:
    idx = n - 1
    if idx <= 9:
        digit = idx
    elif idx <= 189:
        idx_in_2 = idx - 9
        num = 10 + (idx_in_2 - 1) // 2
        rem = (idx_in_2 - 1) % 2

        if rem == 0:
            digit = num // 10
        else:
            digit = num % 10
    else:
        idx_in_3 = idx - 189
        num = 100 + (idx_in_3 - 1) // 3
        rem = (idx_in_3 - 1) % 3

        if rem == 0:
            digit = num // 100
        elif rem == 1:
            digit = (num // 10) % 10
        else:
            digit = num % 10

print("Коля отгадал цифру:", digit)
