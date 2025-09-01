n, h = map(int, input().split())

down = [0] * h
up = [0] * h

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        down[num] += 1
    else:
        up[h - num] += 1

all = []
num = n//2
for i in range(h):
    all.append(num)
    num += up[i]
    num -= down[i]
all = sorted(all)
count = all.count(all[0])
print(all[0], count)