from collections import deque

n, l, r = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

count = 0

# 개방 -> 연산 -> 삽입
# 중요한건 각 그룹별로 다른 연산을 진행해야 함.
# visited는 공통 부분으로 확인, 연산은 현재 위치가 visited에 없으면 진행
# dfs로 전체 나라를 한번씩 탐색하면서 이중 포문이 끝날때에 하루가 지난다고 판단하면 될듯.
while True:
    g_visited = set()
    len_g = False
    for i in range(n):
        for j in range(n):
            l_visited = set()
            if (i, j) not in g_visited and (i, j) not in l_visited:
                peoples = 0
                dfs = deque([(i, j)])
                while dfs:
                    x, y = dfs.popleft()
                    peoples += graph[x][y]
                    l_visited.add((x, y))
                    for a, b in (-1, 0), (0, 1), (1, 0), (0, -1):
                        nx, ny = x+a, y+b
                        if 0<=nx<n and 0<=ny<n:
                            if (nx, ny) not in l_visited and (nx, ny) not in g_visited and l<=abs(graph[x][y] - graph[nx][ny])<=r:
                                dfs.append((nx, ny))
                                dfs = deque(list(set(dfs)))

            if l_visited:
                if len(l_visited) > 1:
                    len_g = True
                g_visited.update(l_visited)
                peoples = int(peoples / len(l_visited))
                while l_visited:
                    x, y = l_visited.pop()
                    graph[x][y] = peoples
    
    if len_g:
        count += 1
    else:
        break

print(count)