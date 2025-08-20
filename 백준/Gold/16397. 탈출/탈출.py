from collections import deque

N, T, G = map(int, input().split())

def btnA(x):
    return x + 1 if x < 99999 else -1

def btnB(x):
    y = x * 2
    if y > 99999:
        return -1
    y -= 10 ** (len(str(y)) - 1)
    return y

visited = [False] * 100000
queue = deque([(N, 0)])  # (현재값, 누른 횟수)
visited[N] = True

answer = "ANG"
while queue:
    x, cnt = queue.popleft()
    if cnt > T:
        break
    if x == G:
        answer = cnt
        break
    
    # 버튼 A
    nx = btnA(x)
    if nx != -1 and not visited[nx]:
        visited[nx] = True
        queue.append((nx, cnt + 1))
    
    # 버튼 B
    nx = btnB(x)
    if nx != -1 and not visited[nx]:
        visited[nx] = True
        queue.append((nx, cnt + 1))

print(answer)