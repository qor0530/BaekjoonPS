from heapq import heappush, heappop

n, k = map(int, input().split())
jewel = []
for _ in range(n):
    m, v = map(int, input().split())
    jewel.append((m, v))

bag = [int(input()) for _ in range(k)]

jewel.sort(key=lambda x: x[0])  # 무게 기준 정렬
bag.sort()  # 오름차순 정렬

cost = 0
values = []
idx = 0  # jewel 인덱스

for c in bag:
    while idx < n and jewel[idx][0] <= c:
        heappush(values, -jewel[idx][1])
        idx += 1
    if values:
        cost += -heappop(values)

print(cost)
