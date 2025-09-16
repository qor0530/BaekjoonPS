import math

epsilon = 1e-7

def is_equal(a, b):
    return math.isclose(a, b, abs_tol=epsilon)

def distance(xa, ya, xb, yb):
    return math.hypot(xa - xb, ya - yb)

def clamp(val, minimum, maximum):
    return max(minimum, min(maximum, val))

def angle(a, b, c):
    val = (b*b + c*c - a*a) / (2 * b * c)
    val = clamp(val, -1, 1)
    return math.degrees(math.acos(val))

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

A = distance(x1, y1, x2, y2)
B = distance(x2, y2, x3, y3)
C = distance(x3, y3, x1, y1)

sides = [A, B, C]
sides.sort()

if sides[2] >= sides[0] + sides[1] - epsilon:
    print("X")
    exit()

a = angle(A, B, C)
b = angle(B, C, A)
c = angle(C, A, B)

angles = [a, b, c]
max_angle = max(angles)

unique_sides = len(set([round(s, 7) for s in sides]))

if unique_sides == 1:
    print("JungTriangle")
elif unique_sides == 2:
    if max_angle > 90 + epsilon:
        print("Dunkak2Triangle")
    elif abs(max_angle - 90) < epsilon:
        print("Jikkak2Triangle")
    else:
        print("Yeahkak2Triangle")
else:
    if max_angle > 90 + epsilon:
        print("DunkakTriangle")
    elif abs(max_angle - 90) < epsilon:
        print("JikkakTriangle")
    else:
        print("YeahkakTriangle")
