import math
n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    radius = r1 + r2
    if d > r1 + r2 or d < abs(r1-r2):
        print(0)
    elif d == radius or d == abs(r1 - r2):
        print(1)
    elif radius > d and d > abs(r1-r2):
        print(2)