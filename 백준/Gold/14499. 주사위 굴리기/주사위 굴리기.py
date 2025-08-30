from collections import deque

# 주사위 알고리즘
#   2
# 4 1 3
#   5
#   6

paths = [(0, 1), (0, -1), (-1, 0), (1, 0)] # 동서북남

n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

cmds = list(map(int, input().split()))

가로 = deque([0, 0, 0])
세로 = deque([0, 0, 0, 0])

for cmd in cmds:
    a, b = paths[cmd - 1]
    nx, ny = x + a, y + b
    if 0<=nx<n and 0<=ny<m:
        x, y = nx, ny
        # move and floor check and print
        # move
        if cmd == 1:
            가로.appendleft(가로.pop())
            세로[1] = 가로[1]
            a, b = 세로.pop(), 가로.popleft()
            가로.appendleft(a), 세로.append(b)
        elif cmd == 2:
            가로.append(가로.popleft())
            세로[1] = 가로[1]
            a, b = 가로.pop(), 세로.pop()
            세로.append(a), 가로.append(b)
        elif cmd == 3:
            세로.append(세로.popleft())
            가로[1] = 세로[1]
        elif cmd == 4:
            세로.appendleft(세로.pop())
            가로[1] = 세로[1]
        # floor check
        if graph[nx][ny] == 0:
            # 주사위 바닥면을 graph[nx][ny]에 복사
            graph[nx][ny] = 세로[3]
        else:
            # graph[nx][ny]를 주사위 바닥면에 복사
            세로[3] = graph[nx][ny]
            graph[nx][ny] = 0
        print(세로[1])