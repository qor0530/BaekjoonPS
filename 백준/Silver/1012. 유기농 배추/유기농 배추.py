import sys
input = sys.stdin.readline
T = int(input().rstrip())
    
for _ in range(T):
    visited = []
    pos = []
    count = 0
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
        pos.append((x, y))
    for x, y in pos:
        Q = []
        if (x, y) not in visited:
            Q.append((x, y))
            count += 1
        while Q:
            pos_x, pos_y = Q.pop(0)
            if (pos_x, pos_y) not in visited:
                visited.append((pos_x, pos_y))
            for new_x, new_y in [(0, 1),(1, 0), (0, -1), (-1, 0)]:
                nx = pos_x + new_x
                ny = pos_y + new_y
                if 0 <= nx < M and 0 <= ny < N:
                    if (nx, ny) not in visited and graph[ny][nx] == 1:
                        visited.append((nx, ny))
                        Q.append((nx, ny))
    print(count)