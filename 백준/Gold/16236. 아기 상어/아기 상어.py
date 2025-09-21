from collections import deque

n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]

sx = sy = -1
for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            sx, sy = i, j
            sea[i][j] = 0

size = 2      # 상어 크기
eat = 0       # 지금까지 먹은 수
time = 0      # 총 시간

while True:
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0

    candidates = []   # (distance, row, col)
    min_dist = None

    # BFS로 모든 도달 가능한 칸 탐색, 먹을 수 있는 물고기 후보 수집
    while q:
        x, y = q.popleft()
        # 이미 최소거리 후보를 찾았고 현재 칸의 거리가 그보다 크면 더 볼 필요 없음
        if min_dist is not None and dist[x][y] > min_dist:
            break
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:  # 상,좌,우,하 (방향 순서는 상->좌 우선 규칙에 영향 없음; 후보에서 정렬할 것)
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                # 이동 가능한 칸: 빈칸(0) 또는 자신보다 작거나 같은 물고기(<= size)
                if sea[nx][ny] <= size:
                    dist[nx][ny] = dist[x][y] + 1
                    if 0 < sea[nx][ny] < size:
                        # 먹을 수 있는 후보
                        d = dist[nx][ny]
                        if min_dist is None or d < min_dist:
                            min_dist = d
                        candidates.append((d, nx, ny))
                    q.append((nx, ny))

    if not candidates:
        # 더 이상 먹을 수 있는 물고기 없음
        break

    # 최소 거리(min_dist)인 후보들만 골라 행->열 기준으로 정렬해서 선택
    reachable = [(r, c) for d, r, c in candidates if d == min_dist]
    reachable.sort()  # (row, col) 순으로 정렬
    tx, ty = reachable[0]

    # 이동 및 상태 갱신
    time += min_dist
    sx, sy = tx, ty
    sea[sx][sy] = 0
    eat += 1
    if eat == size:
        size += 1
        eat = 0

print(time)
