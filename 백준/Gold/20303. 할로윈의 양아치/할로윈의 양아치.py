from collections import defaultdict, deque

n, m, k = map(int, input().split())
c = [0] + list(map(int, input().split()))
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

kids = []
visited = set()

for i in range(1, n + 1):
    if i not in visited:
        que = deque([i])
        group_size = 0
        candy_sum = 0
        while que:
            now = que.popleft()
            if now not in visited:
                visited.add(now)
                group_size += 1
                candy_sum += c[now]
                for next in graph[now]:
                    if next not in visited:
                        que.append(next)
        kids.append((group_size, candy_sum))

dp = [0] * (k)

for weight, value in kids:
    for w in range(k - 1, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[k - 1])
