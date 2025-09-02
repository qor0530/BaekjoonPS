import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))

start, end = map(int, sys.stdin.readline().split())
INF = float('inf')
dist = [INF] * (n+1)
dist[start] = 0
hq = []
heapq.heappush(hq, (0, start))  # (비용, 노드)

while hq:
    cost, now = heapq.heappop(hq)
    if dist[now] < cost:
        continue
    for nxt, w in graph[now]:
        if dist[nxt] > cost + w:
            dist[nxt] = cost + w
            heapq.heappush(hq, (dist[nxt], nxt))

print(dist[end])