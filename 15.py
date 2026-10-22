n, k, m = map(int, input().split())
dist1 = abs(k - m)
dist2 = n - dist1
r = min(dist1, dist2) - 1

print(r)


