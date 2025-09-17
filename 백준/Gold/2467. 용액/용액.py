from heapq import heappop, heappush
n = int(input())

liq = list(map(int, input().split()))

maxhp = []
minhp = []

for i in range(n):
    heappush(maxhp, -liq[i])
    heappush(minhp, liq[i])

min_x = heappop(minhp)
max_x = -heappop(maxhp)

visited = set()

reaching = float("inf")

visited.add(min_x)
visited.add(max_x)

while True:
    score = min_x + max_x
    ab_s = abs(score)
    if ab_s < reaching:
        reaching = ab_s
        a = min_x
        b = max_x
    if score == 0:
        break
    elif score < 0:
        min_x = heappop(minhp)
        if min_x in visited:
            break
        else:
            visited.add(min_x)
    else:
        max_x = -heappop(maxhp)
        if max_x in visited:
            break
        else:
            visited.add(max_x)

print(a, b)