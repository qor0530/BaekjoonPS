import heapq
from collections import defaultdict

n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

def dijkstra(graph, start, n):
    INF = float('inf')
    dist = [INF] * (n + 1) # 원래 다익스트라-힙 구현에서는 그래프에 있는 노드만 찾아 비교
    dist[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if dist[current_node] < current_dist:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    return dist

for i in range(1, n + 1):
    dist = dijkstra(graph, i, n)
    for j in range(1, n + 1):
        if dist[j] == float('inf'):
            print(0, end=' ')
        else:
            print(dist[j], end=' ')
    print()
