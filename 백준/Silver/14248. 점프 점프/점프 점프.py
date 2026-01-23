from collections import deque

n = int(input())
rock = list(map(int, input().split()))
s = int(input())
que = deque([s-1])
visited = []
count = 0
while que:
    now = que.popleft()
    count += 1
    visited.append(now)
    step = []
    for x in [-rock[now], rock[now]]:
        nx = now + x
        if 0 <= nx < n and nx not in visited:
            que.append(nx)
    
print(count)