import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
people = [[] for _ in range(N + 1)]
know_liar = list(map(int, input().split()))
partys = []
for i in range(M):
  party = list(map(int, input().split()))
  for j in range(1, len(party)):
    for k in range(1, len(party)):
      people[party[j]].append(party[k])
      people[party[k]].append(party[j])
  partys.append(party)

knowlist = [False] * (N+1)

def dfs(node):
  que = deque([node])
  knowlist[node] = True
  while que:
    v = que.popleft()
    for i in people[v]:
      if not knowlist[i]:
        que.append(i)
        knowlist[i] = True

for i in range(1, len(know_liar)):
    dfs(know_liar[i])

count = 0
for party in partys:
    counting = True
    for i in range(1, len(party)):
        if knowlist[party[i]]:
            counting = False
            break
    if counting:
        count += 1
print(count)