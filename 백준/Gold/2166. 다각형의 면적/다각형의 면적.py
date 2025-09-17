n = int(input())

pos = []

for i in range(n):
    pos.append(list(map(int, input().split())))

S = 0

for i in range(n-2):
    x1, y1 = pos[0]
    x2, y2 = pos[i+1]
    x3, y3 = pos[i+2]
    
    S += ((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)) / 2

print(round(abs(S), 1))