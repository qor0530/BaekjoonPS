from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

moves = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

q = deque([(r1, c1, 0)])
visited = set([(r1, c1)])

answer = -1

while q:
    x, y, count = q.popleft()

    if x == r2 and y == c2:
        answer = count
        break

    for a, b in moves:
        ax, by = x + a, y + b

        if 0 <= ax < n and 0 <= by < n and (ax, by) not in visited:
            visited.add((ax, by))
            q.append((ax, by, count + 1))

print(answer)