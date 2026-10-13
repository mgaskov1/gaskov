a,b,c,d=map(int,input("Введите четыре целых числа ").split())
if max(a,b,c,d)==a:
    print("Наибольшее число",a)
elif max(a,b,c,d)==b:
    print("Наибольшее число", b)
elif max(a,b,c,d)==c:
    print("Наибольшее число", c)
elif max(a,b,c,d)==d:
    print("Наибольшее число", a)
max=a
print(max)