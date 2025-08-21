from collections import deque
n, m = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

now = deque([(0, 0)])
visited = [[0]*m for _ in range(n)]
while now:
    x, y = now.popleft()
    count = visited[x][y]
    if x == n-1 and y == m-1:
        print(count+1)
        break
    visited[x][y] = True
    for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #상 하 좌 우
        c = x + a
        d = y + b
        if c >= 0 and c < n and d >= 0 and d < m and (c, d):
            if graph[c][d] == 1 and visited[c][d] == 0:
                visited[c][d] = count + 1 
                now.append((c, d))
        