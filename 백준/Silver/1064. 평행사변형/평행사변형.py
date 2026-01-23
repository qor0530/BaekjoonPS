from math import atan2, pi

x1, y1, x2, y2, x3, y3 = map(int, input().split())
A = [x1, y1]
B = [x2, y2]
C = [x3, y3]

# 추론 1. A, B, C가 각도를 이룰 것이다. (아님 -1)
# 추론 2. 나온다면, 3개의 점이 나올 것이다. 

def line_length(ax, ay, bx, by):
    return ((ax-bx)**2 + (ay-by)**2)**(0.5)


if (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1):
    print(-1)
else:
    #2-1. 3개의 점은 각 A,B,C 간의 거리, 하지만 점 위치를 찾을 필요는 없음.
    #2-2. (A-B)*2 + (B-C)*2 이런 식으로 3점의 둘레 비교
    circum = []
    circum.append(line_length(x1, y1, x2, y2)*2 + line_length(x2, y2, x3, y3)*2)
    circum.append(line_length(x1, y1, x2, y2)*2 + line_length(x3, y3, x1, y1)*2)
    circum.append(line_length(x2, y2, x3, y3)*2 + line_length(x3, y3, x1, y1)*2)

    print("%0.9f" % (max(circum) - min(circum)))