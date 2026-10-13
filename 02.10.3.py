m=int(input())
if m>12:
    print("Неверный номер месяца.")
if (m>=1 and m<3) or m==12:
    print("Зима.")
elif m>=3 and m<6:
    print("Весна.")
elif m>=6 and m<9:
    print("Лето.")
elif m>=9 and m<12:
    print("Осень.")
