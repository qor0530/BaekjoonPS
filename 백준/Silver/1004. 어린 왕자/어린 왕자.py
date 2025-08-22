import math

T = int(input())

c = []

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())
        # 원안에 시작점, 도착점이 있는지만 확인하면 됨. 
        # 원안에 있다 -> (반지름 - 점과 원 사이의 거리) > 0, and 둘다 원안에 없어야 함.
        d1 = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        d2 = math.sqrt((x2-cx)**2 + (y2-cy)**2)
        if (r - d1) > 0 and (r - d2) > 0:
            pass
        elif (r - d1) < 0 and (r - d2) < 0:
            pass
        else:
            count += 1
    c.append(count)

print(*c, sep='\n')