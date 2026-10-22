import math
s=input()
n, k, m  = map(int, s.split(' '))
if 2>math.ceil(2*n/k):
    print(2*m)
else:
    print(m*(math.ceil(2*n/k)))

