n = input()
if n[0]=="a" or n[0]=="c" or n[0]=="e" or n[0]=="g":
    s=1
else:
    s=2
if (s+int(n[1]))%2==0:
    print("чёрный")
else:
    print("белый")



