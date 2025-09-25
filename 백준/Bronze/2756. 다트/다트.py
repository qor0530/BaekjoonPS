import math

t=int(input())

def dat(x, y):
    cm = math.sqrt(x**2 + y**2)
    if cm <= 3:
        return 100
    elif cm <= 6:
        return 80
    elif cm <= 9:
        return 60
    elif cm <= 12:
        return 40
    elif cm <= 15:
        return 20
    else:
        return 0

for _ in range(t):
    pos = list(map(float, input().split()))
    me = 0
    yours = 0
    for i in range(0, 12, 2):
        if i < 6:
            me += dat(pos[i], pos[i+1])
        else:
            yours += dat(pos[i], pos[i+1])
    if me == yours:
        print(f"SCORE: {me} to {yours}, TIE.")
    elif me > yours:
        print(f"SCORE: {me} to {yours}, PLAYER 1 WINS.")
    else:
        print(f"SCORE: {me} to {yours}, PLAYER 2 WINS.")