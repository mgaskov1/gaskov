a=int(input("Возраст Антона: "))
b=int(input("Возраст Бориса: "))
c=int(input("Возраст Виктора: "))
if a>b and a>c:
    print("Антон страше всех.")
elif b>a and b>c:
    print("Борис старше всех.")
elif c>a and c>b:
    print("Виктор старше всех.")
elif a==b and b>c:
    print("Антон и Борис старше Виктора")
elif a==c and c>b:
    print("Антон и Виктор старше Бориса")
elif b==c and b>a:
    print("Борис и Виктор старше Антона")
elif a==b and c==a:
    print("Одного возраста.")

