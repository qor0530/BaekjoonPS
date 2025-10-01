from collections import deque
from itertools import combinations
import copy

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

w_list = []
virus = deque()
result=0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 0:
            w_list.append((i, j))
wall = list(combinations(w_list, 3))

for i in range(len(wall)):
    l_v = copy.deepcopy(virus)
    l_g = copy.deepcopy(graph)
    for a, b in wall[i]:
        l_g[a][b] = 1
    while l_v:
        x, y = l_v.popleft()
        l_g[x][y] = 2
        for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #상하좌우
            ax, by = x+a, y+b
            if 0 <= ax < n and 0 <= by < m:
                if l_g[ax][by] == 0:
                    l_v.append((ax, by))
    count = 0
    for i in range(n):
        for j in range(m):
            if l_g[i][j] == 0:
                count += 1
    if count > result:
        result = count
print(result)