from heapq import heappop, heappush

import sys
sys.setrecursionlimit(10**7)

v, e = map(int, input().split())

hp = []

parent = [i for i in range(v+1)]

def find(a):
    if parent[a] != a:
        return find(parent[a])
    else:
        return a

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa > pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

for i in range(e):
    A, B, C = map(int, input().split())
    heappush(hp, ((C, A, B)))

weight = 0
while hp:
    c, a, b = heappop(hp)
    if find(a) != find(b):
        weight += c
        union(a, b)

print(weight)