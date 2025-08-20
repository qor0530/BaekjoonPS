N, L = map(int, input().split())

sin = []

for i in range(N): 
    sin.append(list(map(int, input().split())))

t = 0
dis = 0
D, R, G = sin.pop(0)
while dis < L:
    if D < dis and sin:
        D, R, G = sin.pop(0)
    if t % (R+G) >= R or D != dis:
        dis += 1
    t += 1
print(t)