p=input()
if (len(p)!=4)or(1900 <= int(p) <= 2050)or(len(set(p)) != 4):
    print("ERROR")
else:
    print("OK")
