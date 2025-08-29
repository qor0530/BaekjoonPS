from collections import deque

n = int(input())
k = int(input())
apple = []
for i in range(k):
    x, y = map(int, input().split())
    apple.append((x-1, y-1))

l = int(input())
direction = {}
for i in range(l):
    t, sign = input().split()
    direction[int(t)] = sign

snake = deque([(0, 0)])
v = 1
d = [(-1, 0), (0,1), (1, 0), (0, -1)] # 상 우 하 좌
t = 0
loop = True
while loop:
    t+=1
    x, y = snake.pop()
    nx = x + d[v][0]
    ny = y + d[v][1]
    if n > nx >= 0 and n > ny >= 0:
        if (nx, ny) not in snake:
            pass
        else:
            loop = False
    else:
        loop = False

    snake.append((x, y))
    if (nx, ny) in apple:
        apple.pop(apple.index((nx,ny)))
    else:
        snake.popleft()
    snake.append((nx, ny))

    try:
        if direction[t] == 'D':
            v = (v + 1) % 4
        else:
            v = (v + 3) % 4
    except:
        pass
print(t)