from collections import deque

n = int(input())
room = [list(map(int, input())) for _ in range(n)]

x, y = 0, 0

visited = [[False] * n for _ in range(n)]
num = []
for i in range(n):
    for j in range(n):

        if room[i][j] == 1 and not visited[i][j]:
            dfs = deque([(i, j)])
            count = 0
            while dfs:
                x, y = dfs.popleft()
                visited[x][y] = True
                count += 1
                for a, b in [-1, 0], [0, -1], [1, 0], [0, 1]: # 상 좌 하 우
                    if x+a >= 0 and x+a < n and y+b >= 0 and y+b < n and not visited[x+a][y+b] and room[x+a][y+b] == 1:
                        dfs.append((x+a, y+b))
                dfs = deque(set(dfs))
            num.append(count)

print(len(num))
num = sorted(num)
print(*num, sep='\n')