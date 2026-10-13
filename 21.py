s=input()
n, m = s.split("-")
if n[0]=="a":
    s1=1
elif n[0]=="b":
    s1=2
elif n[0]=="c":
    s1=3
elif n[0]=="d":
    s1=4
elif n[0]=="e":
    s1=5
elif n[0]=="f":
    s1=6
elif n[0]=="g":
    s1=7
elif n[0]=="h":
    s1=8

if m[0] == "a":
    s2 = 1
elif m[0] == "b":
    s2 = 2
elif m[0] == "c":
    s2 = 3
elif m[0] == "d":
    s2 = 4
elif m[0] == "e":
    s2 = 5
elif m[0] == "f":
    s2 = 6
elif m[0] == "g":
    s2 = 7
elif m[0] == "h":
    s2 = 8
if (abs(s1-s2)==1 and (abs(int(n[1])-int(m[1]))==2))or(abs(s1-s2)==2 and (abs(int(n[1])-int(m[1]))==1)):
    print("верно")
else:
    print("ошибка")


