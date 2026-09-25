#1,5
"""print("Привет, Python!\nHello, Python!\nBonjour Python!\nHej, Python!\nHola, Python!")"""
#2
"""print("Привет","Python!",sep=" ")"""
#3
"""s, r = map(int, input().split())
print(s+r)"""
#4
"""print("(|___/)")
print("(='.'=)")
print('(")_(")')"""
#6
"""name=input("Как вас зовут?")
print("Здравствуйте,",name)
like=input("Что Вам нравится?")
print("Отлично!",like,"- хорошее увлечение")"""
#7
"""l=input("Login: ")
p=input("Password: ")
n=input("New password: ")
print("User",l,"has changed the password to",n)"""
#8
"""print("Введите плей-лист папы")
a=input()
b=input()
c=input()
d=input()
e=input()
print("Плей-лист мамы")
print(e,d,c,b,a,sep="\n")"""
#9
"""a=input("номер рейса: ")
b=input("название авиакомпании (на русском языке): ")
c=input("название авиакомпании (на английском языке): ")
d=input("город прилета (на русском языке): ")
e=input("город прилета (на английском языке): ")
print("Заканчивается посадка на рейс",a,b,"до",d)
print("This is the final boarding call for",c,"flight",a,"to",e)"""
#10
"""s=int(input("Общая стоимость часов "))
x=(s-96*48)/6
print(x)"""
#11
"""import math
r1=int(input())
r2=int(input())
s=(math.pi)*max(r1,r2)**2-(math.pi)*min(r1,r2)**2
print(s)"""
#12
"""a=int(input())
s=((a+2)*3-6)/3-4
d=a-4
print(s,d)"""
#13
"""a=float(input())
a1=a/2.54
a2=a1/12
a3=a2/3
a4=a3/1760
print(a3,"ярдов")
print(a4,"миль")
print(a2,"футов")
print(a1,"дюймов")"""
#14
"""a=input()
a1,a2=a.split()
print(a1)
print(a2)"""
#15
"""i = 1
man = 1
w = 7
c = w * 7 * 7
k = c * 7
total = i+man+w+c+k
print(total)"""
#24
"""n=int(input())
print(n%2)"""
#26
"""n=int(input())
print("(|___/) "*n)
print("(='.'=) "*n)
print('(")_(") '*n)"""
#27
"""k=str(input())
n=int(input())
r=int(input())
print(int(k*n)*r)"""
#28
"""raw = input('Enter number:')
num = str(raw)
print(num)"""
#29
"""import math
a=int(input())
b=int(input())
c=int(input())
a1=math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
b1=math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
c1=math.degrees(math.acos((b**2 + a**2 - c**2) / (2 * b * a)))
print(a1,b1,c1)"""
#30
"""itn=int(input("int:"))
att=int(input("att:"))
td=int(input("td:"))
comp=int(input("comp:"))
yds=int(input("yds:"))
a = ((comp / att) - 0.3) * 5
b = ((yds / att) - 3) * 0.25
c = (td / att) * 20
d = 2.375 - ((itn / att) * 25)
pr=((a+b+c+d)/6)*100
print(pr)"""
#31
"""x=int(input())
y=int(input())
print((x%y)*(y%x)+1)"""
#32
"""n=float(input())
h=n//30
m=(n%30)*2
print(int(h),":",int(m))"""
#33
"""x=int(input())
y=int(input())
c=int(input())
s=x*y
n=c//s +1
print("Страница:",n)"""
