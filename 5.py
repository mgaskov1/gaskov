s=input("Счёт ребят: ")
k,a,c  = map(int, s.split(' '))
m=k
if a>m:
    m=a
if c>m:
    m=c
print(m)