r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

visited = {chr(ord('A') + i): False for i in range(26)}

def dfs(x, y, count):
    global answer
    answer = max(answer, count)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            char = board[nx][ny]
            if not visited[char]:
                visited[char] = True
                dfs(nx, ny, count + 1)
                visited[char] = False  # 백트래킹

# 시작 위치 방문 표시
visited[board[0][0]] = True
dfs(0, 0, 1)

print(answer)
