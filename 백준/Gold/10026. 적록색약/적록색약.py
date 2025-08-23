from collections import deque
n = int(input())

pic = [list(input()) for _ in range(n)]

visited = [[False]* n for _ in range(n)]

gc1 = 0
gc2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            type = pic[i][j]
            dfs = deque([(i, j)])
            gc1 += 1
            while dfs:
                x, y = dfs.popleft()
                visited[x][y] = True
                for a, b in [(-1, 0), (0, -1), (1, 0), (0, 1)]: #상 좌 하 우
                    nx, ny = x+a, y+b
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        if not visited[nx][ny] and type == pic[nx][ny]:
                            dfs.append((nx, ny))
                dfs = deque(set(dfs))

visited = [[False]* n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if pic[i][j] == 'G':
            pic[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            type = pic[i][j]
            dfs = deque([(i, j)])
            gc2 += 1
            while dfs:
                x, y = dfs.popleft()
                visited[x][y] = True
                for a, b in [(-1, 0), (0, -1), (1, 0), (0, 1)]: #상 좌 하 우
                    nx, ny = x+a, y+b
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        if not visited[nx][ny] and type == pic[nx][ny]:
                            dfs.append((nx, ny))
                dfs = deque(set(dfs))

print(gc1, gc2)