import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [(n+1) * [0] for i in range(n+1)]
nlist = [i for i in range(1, n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

numlist = []

def bfs(start_v):
  discoverd = [start_v]
  queue = deque()
  queue.append(start_v)

  while queue:
    v = queue.popleft()
    for w in range(len(graph[start_v])):
      if graph[v][w] == 1 and (w not in discoverd):
        discoverd.append(w)
        queue.append(w)
  return discoverd
start = 1
count = 0
while len(numlist) != n:
    count += 1
    complement = list(set(nlist) - set(numlist))
    numlist += bfs(complement[0])

print(count)